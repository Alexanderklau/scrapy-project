import scrapy
from ..items import GamemessagespiderItem
from scrapy.selector import Selector
import json

class Game_Spider(scrapy.Spider):
    name = 'game'
    start_urls = []
    for i in range(1,2):
        url = 'http://down.gamersky.com/page/pc/0-0-0-0-0-0-0-00_' + str(i) + '.html'
        start_urls.append(url)

    def parse_star(self,response):
        item1 = response.meta['item']
        wb_data = response.body.decode('utf-8')
        s = str(wb_data[7:-2])
        js = json.loads(s)
        item1['star'] = js['Average']
        return item1
        # star = wb_data[1][:-2]
        # js = json.loads(str(star))

        # for jst in js:
        #     item1['star'] = jst['Average']
        #     return item1

    def parse(self, response):
        sel = Selector(response)
        games = sel.xpath('//html/body/div/ul/li')
        for game in games:
            item1 = GamemessagespiderItem()
            item1['name'] = game.xpath('//div[2]/a/text()').extract()
            item1['date'] = game.xpath('//div[3]/text()').extract()
            item1['launage'] = game.xpath('//div[4]/text()').extract()
            item1['type'] = game.xpath('//div[4]/text()').extract()
            ID = game.xpath('//div[6]/@data-generalid').extract()
            for id in ID:
                url = 'http://i.gamersky.com/apirating/init?callback=jQuery&generalId=' + str(id)
                # list_a = response.urljoin(url)
                yield scrapy.Request(url,meta={'item':item1},callback=self.parse_star)


#http://i.gamersky.com/apirating/init?callback=jQuery&generalId=365014
