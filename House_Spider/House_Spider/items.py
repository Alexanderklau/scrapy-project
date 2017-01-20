# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HouseSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    #名称
    HouseName = scrapy.Field()
    #信息
    HouseMessage = scrapy.Field()
    #价格
    HousePrice = scrapy.Field()
    #地域
    HouseArea = scrapy.Field()
    #类型
    Housetype = scrapy.Field()
    #楼层
    HouseTool = scrapy.Field()
    #地址
    HouseAdderss = scrapy.Field()
    #联系人
    HouseContent = scrapy.Field()
    #url
    PhoneNumber = scrapy.Field()
