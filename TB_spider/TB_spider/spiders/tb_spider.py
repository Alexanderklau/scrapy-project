# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
from ..items import TbSpiderItem
from scrapy.selector import Selector
import scrapy

class Tmgoods_spider(scrapy.Spider):
    name = 'TM'
    allowed_domains = ["http://www.tmall.com"]
    start_urls = (
        'http://list.tmall.com/search_product.htm?type=pc&totalPage=100&cat=50025135&sort=d&style=g&from=sn_1_cat-qp&active=1&jumpto=10#J_Filter',
    )
    counts = 0
    def parse(self, response):
        Tmgoods_spider.counts += 1
        divs = response.xpath("//div[@id='J_ItemList']/div[@class='product']/div")
        if not divs:
            self.log("ERROR -- %s"%response.url)
        for div in divs:
            item = TbSpiderItem()
            item['GOODS_PRICE'] = div.xpath("p[@class='productPrice']/em/@title")[0].extract()
            item['GOODS_NAME'] = div.xpath("p[@class='productTitle']/a/@title")[0].extract()
            good_urls = div.xpath("p[@class='productTitle']/a/@href")[0].extract()
            item['GOODS_URL'] = good_urls if "http:" in good_urls else ("http:" + good_urls)
            # return item
            # if this url have 'http:' string,keep original url,on the contrary,add 'http:' string
            yield scrapy.Request(url=item['GOODS_URL'],meta={'item':item},callback=self.parse_company,)
    def parse_company(self,response):
        div = response.xpath('//div[@class="extend"]/ul')
        if not div:
            self.log("ERROR -- %s"%response.url)
        item = response.meta['item']
        div = div[0]
        item['SHOP_NAME'] = div.xpath('li[1]/div[@class="right"]/a/text()')[0].extract()
        item['SHOP_URL'] = div.xpath('li[1]/div[@class="right"]/a/@href')[0].extract()
        item['COMPNY_ADDRESS'] = div.xpath('li[3]/div/text()')[0].extract().strip()
        return item




