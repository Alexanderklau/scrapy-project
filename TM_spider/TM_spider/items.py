# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TmSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    good_name = scrapy.Field()
    good_price = scrapy.Field()
    good_comany = scrapy.Field()
    good_volme = scrapy.Field()
