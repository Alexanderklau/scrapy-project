import re
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
        def parse_getCommentnum(self, response):
            item1 = response.meta['item']
            js = json.loads(str(response.body))
            item1['score1count'] = js['productCommentSummary'][0]['goodCount']
            num = item1['ID']
            s1 = str(num)
            #https://p.3.cn/prices/mgets?callback=jQuer&pdpin=&pdbp=0&skuIds=J_2385681
            url = "https://p.3.cn/prices/mgets?callback=jQuer&pdpin=&pdbp=0&skuIds=J_" + s1[3:-2]
            yield scrapy.Request(url, meta={'item': item1}, callback=self.parse_price)
        def parse_detail(self, response):
            item1 = response.meta['item']
            sel = Selector.response()

            temp = response.body.split('commentVersion:')
            pattern = re.compile("[\'](\d+)[\']")
            if len(temp) < 2:
                item1['commentVersion'] = -1
            else:
                match = pattern.match(temp[1][:10])
                item1['commentVersion'] = match.group()
            #https://club.jd.com/comment/productPageComments.action?
            #callback=fetchJSON_comment98vv59634&productId=3245084
            #&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0
            url = "https://club.jd.com/comment/productPageComments.action?callback=fetchJSON_comment98vv59634&productId=" + str(item1['ID'][0]) + "&score=0&sortType=5&page=0&pageSize=10&isShadowSku=0"
            yield scrapy.Request(url,meta={'item':item1},callback=self.parse_getCommentnum)


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

