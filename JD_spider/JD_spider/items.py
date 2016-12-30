# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JdSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class goodsItem(scrapy.Item):
    link = scrapy.Field()
    ID = scrapy.Field()
    name = scrapy.Field()
    price = scrapy.Field()
    comment_num = scrapy.Field()
    shop_name = scrapy.Field()
    commentVersion = Field()


