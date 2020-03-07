import scrapy
import re
from dofus_scrapy.items import DofusScrapyItem 
from scrapy import Spider


class dofusscrapy(scrapy.Spider):
    name = "dofusscrapy"


    def start_requests(self):

        for i in range(1, 7):
            url = 'https://www.dofus.com/fr/mmorpg/encyclopedie/monstres?text=&monster_level_min=1&monster_level_max=1600&monster_type[0]=boss&page=' + str(i)
            yield scrapy.Request(url = url, callback=self.parse)
    

    def parse(self, response):
        domain = 'https://www.dofus.com'
        content = response.css('span.ak-linker')
        url_list = content.xpath('a//@href').extract()
        for url in url_list:
            yield scrapy.Request(url = domain+url, callback=self.extract_content)
    

    def extract_content(self, response):
        content = response.xpath('//html')
        name = content.xpath('//meta[@property="og:title"] /@content').extract_first()
        stats = content.css('div.ak-title')
        stats = stats.xpath('span//text()').extract()
        level = content.xpath("//*[contains(@class, 'col-xs-4 text-right ak-encyclo-detail-level')]/text()").extract_first()
        quetes = content.xpath("//*[contains(@class, 'ak-panel-content')]/text()")
        quetes = quetes[14].extract()

        monstre = DofusScrapyItem()

        monstre['name'] = name.split(' - ')[0] 
        monstre['level'] = level.split(' : ')[-1]
        monstre['pdv'] = stats[0][4:]
        monstre['pa'] = stats[1][1:]
        monstre['pm'] = stats[2][1:]
        monstre['res_terre'] = stats[3][1:] 
        monstre['res_air'] = stats[4][1:] 
        monstre['res_eau'] = stats[5][1:]
        monstre['res_feu'] = stats[6][1:] 
        monstre['res_neutre'] = stats[7][1:] 
        quetes = {word for keyword in quetes for word in quetes[1:-1].split(",")}
        monstre['quetes'] = list(quetes)

        yield monstre

 