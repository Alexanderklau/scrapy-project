# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TbSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    GOODS_NAME = scrapy.Field()
    GOODS_PRICE = scrapy.Field()
    GOODS_URL = scrapy.Field()
    SHOP_NAME = scrapy.Field()
    SHOP_URL = scrapy.Field()
    COMPNY_ADDRESS = scrapy.Field()
    COMPNY_NAME = scrapy.Field()

