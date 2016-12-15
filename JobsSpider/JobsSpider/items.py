# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobsspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    Jobsname = scrapy.Field() #name
    Jobscatalog = scrapy.Field() #work type
    JobsLocation = scrapy.Field() # work location(工作地点)
    JobsPublishTime = scrapy.Field() #work publish time
    JobsLink = scrapy.Field()
    JobsRick = scrapy.Field()
    JobRequire = scrapy.Field()
    Jobinstry = scrapy.Field()

