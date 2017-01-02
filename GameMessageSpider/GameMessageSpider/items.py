# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GamemessagespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    star = scrapy.Field()
    date = scrapy.Field()
    launage = scrapy.Field()
    type = scrapy.Field()
    ID = scrapy.Field()

