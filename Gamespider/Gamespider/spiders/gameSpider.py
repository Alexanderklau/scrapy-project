import scrapy
from scrapy.selector import Selector
from ..items import GamespiderItem

class GameSpider(scrapy.Spider):
    name = 'game'
    allow_domains = ['3dmgame.com']
    start_urls = [
        'http://www.3dmgame.com/games/hot/'
    ]

    def parse(self, response):
        sel = Selector(response)
        item = GamespiderItem()
        item['GameName'] = sel.xpath('//h3/a/text()').extract()
        item['Gamecontent'] = sel.xpath('//div[@class="info"]/dd').extract()
        item['Gamestar'] = sel.xpath('//div[@class="score"]/div/text()').extract()
        return item