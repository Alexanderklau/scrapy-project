# coding:utf-8
import scrapy
from ..items import GameimageItem

class GameImageSpider(scrapy.Spider):
    name = 'gameimage'
    allowed_domains = []
    start_urls = ['http://pic.ali213.net/list/game/']


    def parse(self,response):
        item = GameimageItem()
        item['imageUrl'] = response.xpath('//img//@src').extract()
        yield item

    def start_requests(self):
        pages = []
        for i in range(2, 20):
            Url = 'http://pic.ali213.net/list/game/index_%s.html' % i
            page = scrapy.Request(Url)
            pages.append(page)
        return pages