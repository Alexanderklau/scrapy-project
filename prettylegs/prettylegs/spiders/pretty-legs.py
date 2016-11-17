# -*- coding: utf-8 -*-
import scrapy
from ..items import PrettylegsItem
import re

class PrettylegsSpider(scrapy.Spider):
    name = 'legs'
    allow_domains = []
    start_urls = ['http://www.mmkao.net/']


    def parse(self, response):
        item = PrettylegsItem()
        item['imageUrl'] = response.xpath('//img//@src').extract()
        item['imageHref'] = response.xpath('//a//@href').extract()
        yield item


