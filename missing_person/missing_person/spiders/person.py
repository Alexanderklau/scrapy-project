from ..items import MissingPersonItem
import scrapy

class misspersonSpider(scrapy.Spider):
    name = 'miss'
    allowed_domains = []
    start_urls = ['http://www.zgxrqsw.com/xrqs.asp']

    def parse(self, response):
        item = MissingPersonItem()
        item['name'] = response.xpath('//a[@target="_blank"]').extract()
        yield item
