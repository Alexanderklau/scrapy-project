import scrapy
from ..items import TestItem
from scrapy.selector import Selector

class DomzSpider(scrapy.Spider):
    name = "domz"
    allowed_domains = ["sina.com"]
    start_urls = [
        "http://www.sina.com.cn/"
    ]

    #def parse(self, response):
     #   for href in response.css("ul.directory.dir-col > li > a::attr('href')"):
      #      url = response.urljoin(response.url, href.extract())
       #     yield scrapy.Request(url, callback=self.parse_dir_contents)

    def parse(self, response):
        sel = Selector(response)
        sites = sel.xpath('//ul[@class="list-a news_top"]/li')
        items = []
        for site in sites:
            item = TestItem()
            item['title'] = site.xpath('a/text()').extract()
            item['link'] = site.xpath('a/@href').extract()
            item['desc'] = site.xpath('text()')
            item.append(item)
        return items
