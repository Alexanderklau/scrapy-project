import scrapy
from ..items import HotgameItem

class HotGameSpider(scrapy.Spider):
    name = 'game'
    allowed_domains = []
    start_urls = ['http://www.ali213.net/zt/ztisitemap_hot.html']


    def parse(self, response):
        items = []
        name_list = response.css('html body div.contain.con.clearfix div.list-con.clearfix div.list-con-main.clearfix')
        for name in name_list:
            item = HotgameItem()
            item['GameName'] = name.xpath('//li//a[@class="item-title"]/text()').extract()
            items.append(item)
        return items

    def start_requests(self):
        pages = []
        for i in range(2,6):
            Url = 'http://www.ali213.net/zt/ztisitemap_hot_p%s.html' %i
            page = scrapy.Request(Url)
            pages.append(page)
        return pages

