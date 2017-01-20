import scrapy
import re
from ..items import HouseSpiderItem
from scrapy.selector import Selector

class House_Spider(scrapy.Spider):
    name = 'Hs'
    start_urls = []
    for i in range(1,10):
        urls = 'http://cd.zu.anjuke.com/fangyuan/p' + str(i) + '/'
        start_urls.append(urls)

    def parse(self, response):
        sel = Selector(response)
        houses = sel.xpath('//div[@id="list-content"]')
        hrs = houses.xpath('div')
        for house in hrs[2:]:
            item1 = HouseSpiderItem()
            item1['HouseName'] = house.xpath('//h3/a/text()').extract()
            item1['HouseTool'] = house.xpath('//p[@class="details-item tag"]/text()[4]').extract()
            item1['Housetype'] = house.xpath('//p[@class="details-item tag"]/text()[1]').extract()
            item1['HousePrice'] = house.xpath('//div[@class="zu-side"]/p/strong/text()').extract()
            item1['HouseMessage'] = house.xpath('//p[@class="details-item tag"]/text()[2]').extract()
            # # item1['HouseAdderss'] = house.xpath('//address[@class="details-item"]/a').extract()
            address = house.xpath('//address[@class="details-item"]/a/text()').extract()
            address = re.sub(r'\s+','',str(address))
            address = re.sub(r'\\n','',address)
            item1['HouseAdderss'] = eval(address)
            area = house.xpath('//address[@class="details-item"]/text()[2]').extract()
            area = re.sub(r'\s+','',str(area))
            area = re.sub(r'\\n','',area)
            area = re.sub(r'［','',area)
            area = re.sub(r'］','',area)
            # print(type(eval(area)))
            item1['HouseArea'] = eval(area)
            item1['HouseContent'] = house.xpath('//p[2]/span/text()').extract()
            return item1
            # # url = house.xpath('//@link').extract()
            # for base_url in response.xpath('//@link'):
            #     list_a = response.urljoin(base_url.extract())
            #     print(list_a)
                # yield scrapy.Request(list_a, meta={'item': item1}, callback=self.parse_Phone)
    # def parse_Phone(self,response):
        # item1 = response.meta['item']
        # sel = Selector(response)
        # item1['PhoneNumber'] = sel.xpath('//div[@class="icon_tel"]/text()').extract()
        # return item1
