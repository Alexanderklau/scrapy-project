# -*-coding:utf-8 -*- 
__author__ = 'Yemilice_lau'
from ..items import TmSpiderItem
import scrapy
class TM_spider(scrapy.Spider):
    name = 'tm'
    allowed_domains = ['http://www.tmall.com']
    start_urls = (
        'https://list.tmall.com/search_product.htm?q=%CA%D6%BB%FA&sort=s&style=g&type=pc'
    )
    def start_requests(self):
        reqs = []
        for i in range(1,2):
            req = scrapy.Request("https://list.tmall.com/search_product.htm?type=pc&q=%CA%D6%BB%FA&totalPage=" + str(i) + "&sort=s&style=g&jumpto=100")
            reqs.append(req)
        return reqs

    def parse(self, response):
        good_list = response.xpath("//div[@id='J_ItemList']/div[@class='product']/div")
        items = []
        if not good_list:
            self.log("ERROR -- %s"%response.url)
        for good in good_list:
            item = TmSpiderItem()
            item['good_name'] = good.xpath('div[@class="productTitle"]/a[1]/text()').extract()
            item['good_price'] = good.xpath('p[@class="productPrice"]/em/@title').extract()
            # item['good_comany'] = good.xpath('div[@class="productShop"]/a/text()').extract()
            # item['good_volme'] = good.xpath('p[@class="productStatus"]/span/em/text()').extract()
            items.append(item)
        return items










# if __name__ == '__main__':