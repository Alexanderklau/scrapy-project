# coding:utf-8
import scrapy
from ..items import GirlimageItem

from scrapy.crawler import CrawlerProcess


class jiandanSpider(scrapy.Spider):
    name = 'Girl'
    allowed_domains = []
    start_urls = ["http://jandan.net/ooxx"]

    def parse(self, response):
        item = GirlimageItem()
        item['image_urls'] = response.xpath('//img//@src').extract()  # 提取图片链接
        # print 'image_urls',item['image_urls']
        yield item
        new_url = response.xpath('//a[@class="previous-comment-page"]//@href').extract_first()  # 翻页
        # print 'new_url',new_url
        if new_url:
            yield scrapy.Request(new_url, callback=self.parse)