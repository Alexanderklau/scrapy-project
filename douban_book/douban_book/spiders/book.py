from ..items import DoubanBookItem
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from scrapy.contrib.linkextractors import LinkExtractor
import scrapy
from scrapy import Request
class DoubanBoook(scrapy.Spider):
    name = 'Book'
    allowed_domains = ['douban.com']
    start_urls = ['https://book.douban.com/tag/%E6%8E%A8%E7%90%86?start=0']

    rules = (
        Rule(LinkExtractor(allow=r'start=\d{1,3}$'),callback='parse_item',follow=True),

    )

    def parse_item(self,response):
        items = []
        book_list = response.xpath('/html/body/div[3]/div[1]/div/div[1]/div/ul')
        for book in book_list:
            item = DoubanBookItem()
            try:
                item['book_name'] = book.xpath('/li[1]/div[2]/h2/a/text()').extract()[0]
                item['book_star'] = book.xpath('/li[3]/div[2]/div[2]/span[2]/text()').extract()
                item['book_people'] = book.xpath('/li[3]/div[2]/div[2]/span[3]/text()').extract()
                item['book_publish'] = book.xpath('/li[3]/div[2]/p/text()').extract()
                desc = book.xpath('/li[3]/div[2]/div[1]/text()').extract()[0].strip().split('/')
                item['book_author'] = '/'.join(desc)
                item['book_referral'] = desc.pop()
                item['book_year'] = desc.pop()
            except:
                pass
            items.append(item)
        return items

    def start_requests(self):
        yield Request("https://book.douban.com/tag/%E6%8E%A8%E7%90%86?start=0",
                      headers={'Connection': 'Keep-Alive',
                               'Accept': 'text/html, application/xhtml+xml, */*',
                               'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
                               'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',})

