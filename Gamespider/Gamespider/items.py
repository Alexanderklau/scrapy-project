# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GamespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    GameName = scrapy.Field()
    Gamecontent = scrapy.Field()
    Gamestar = scrapy.Field()
    pass
