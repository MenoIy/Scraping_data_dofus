# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field

class DofusScrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = Field()
    level = Field()
    pdv = Field()
    pa = Field()
    pm = Field()

    res_terre = Field()
    res_air = Field()
    res_feu = Field()
    res_eau = Field()
    res_neutre = Field()

    quetes = Field()

    pass
