import scrapy
from scrapy.selector import Selector
from ..items import XiciIpItem
import re

class Xici_Spider(scrapy.Spider):
    name = 'XC'
    start_urls = (
        'http://www.xicidaili.com/',
    )
    def start_requests(self):
        reqs = []
        for i in range(1,206):
            req = scrapy.Request("http://www.xicidaili.com/nn/%s"%i)
            reqs.append(req)
        return reqs
    def parse(self, response):
        ip_list = response.xpath('//table[@id="ip_list"]')
        trs = ip_list[0].xpath('tr')
        items = []
        for ip in trs[1:]:
            pre_item = XiciIpItem()
            pre_item['IP'] = ip.xpath('td[2]/text()').extract()
            pre_item['PORT'] = ip.xpath('td[3]/text()').extract()
            pre_item['POSITION'] = ip.xpath('td[4]/a/text()').extract_first(default='不明')
            pre_item['TYPE'] = ip.xpath('td[6]/text()').extract()
            pre_item['SPEED'] = ip.xpath('td[7]/div[@class="bar"]/@title').re('\d{0,2}\.\d{0,}')
            pre_item['LAST_CHECK_TIME'] = ip.xpath('td[10]/text()').extract()
            items.append(pre_item)
        return items
