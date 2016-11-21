# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanBookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    book_name = scrapy.Field()
    book_author = scrapy.Field()
    book_referral = scrapy.Field()
    book_star = scrapy.Field()
    book_publish = scrapy.Field()
    book_people = scrapy.Field()
    book_year = scrapy.Field()

    pass
