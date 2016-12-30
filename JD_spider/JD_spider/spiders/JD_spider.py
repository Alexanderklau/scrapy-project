import scrapy
from ..items import goodsItem
from scrapy.selector import Selector
import json

class JD_spider(scrapy.Spider):
    name = 'JD'
    start_urls = []
    for i in range(1,11):
        url = 'https://list.jd.com/list.html?cat=9987,653,655&page=' + str(i)
        start_urls.append(url)
        def parse_price(self,response):
            item1 = response.meta['item']
            temp1 = response.body.split('jQuery([')
            s = temp1[1][:-4]
            js = json.load(str(s))
            item1['price'] = js['p']
            return item1
        def parse_detail(self, response):
            item1 = response.meta['item']
            sel = Selector.response()

            temp =


        def parse(self, response):
            sel = Selector(response)
            goods = sel.xpath('//li[@class="gl-item"]')
            for good in goods:
                item1 = goodsItem()
                item1['ID'] = good.xpath('./div/@data-sku').extract()
                item1['name'] = good.xpath('./div/div[@class="p-name"]/a/em/text()').extract()
                item1['link'] = good.xpath('./div/div[@class="p-img"]/a/@href').extract()
                url = "http:" + item1['link'][0] + "#comment"
                yield scrapy.Request(url,meta={'item':item1},callback=self.parse_detail)

