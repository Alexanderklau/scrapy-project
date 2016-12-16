# -*- coding: utf-8 -*-
import re
import json
from scrapy.selector import Selector
try:
    from scrapy.spider import Spider
except:
    from scrapy.spider import BaseSpider as Spider
from scrapy.utils.response import get_base_url
from scrapy.utils.url import urljoin_rfc
from scrapy.contrib.spiders import CrawlSpider,Rule

from scrapy.contrib.linkextractors import LinkExtractor
from ..items import JobsspiderItem
class LagouJob(CrawlSpider):
    name = 'Jobs'
    download_delay = 1
    allowed_domains = ["lagou.com"]
    start_urls = ["https://www.lagou.com/zhaopin"]
    rules = [Rule(LinkExtractor(allow=(r'/zhaopin/\d/')),
                  follow=True,callback='parse_item')]

    def parse_item(self,response):
        items = []
        sites = response.xpath("/html/body/div[2]/div[2]/div[1]/div[3]/ul")
        for site in sites:
            item = JobsspiderItem()
            try:
                item['Jobsname'] = site.xpath("//li/div[1]/div[2]/div[1]/a/text()").extract()
                item['Jobscatalog'] = sites.xpath("//li/div[1]/div[1]/div[1]/a/h2/text()").extract()
                item['JobsLocation'] = sites.xpath("//li/div[1]/div[1]/div[1]/a/span/em/text()").extract()
                item['JobsPublishTime'] = site.xpath("//li/div[1]/div[1]/div[1]/span/text()").extract()
                item['JobsLink'] = site.xpath("//li/div[1]/div[1]/div[1]/a/@href").extract()
                item['JobsRick'] = site.xpath("//li/@data-salary").extract()
                item['JobRequire'] = site.xpath("//li/div[2]/div[2]/text()").extract()
                item['Jobinstry'] = site.xpath("//li/div[1]/div[2]/div[2]/text()").extract()
            except:
                pass
            items.append(item)
        return items