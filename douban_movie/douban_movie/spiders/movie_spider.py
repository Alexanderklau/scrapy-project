# coding:utf-8
import scrapy
from ..items import DoubanMovieItem
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
class Movie_spider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['douban.com']
    start_urls = ['https://movie.douban.com/top250?start=0&filter=']
    rules = (
        Rule(LinkExtractor(allow=r'start=\d{1,3}$'), callback='parse_item', follow=True),

    )

    def parse(self, response):
        items = []
        movie_list = response.xpath("/html/body/div[3]/div[1]/div/div[1]/ol")
        for movie in movie_list:
            item = DoubanMovieItem()
            try:
                desc = movie.xpath("//li//div//div[2]//div[1]//a//text()").extract()[0].strip().split('/')
                
                item['movie_star'] = response.xpath("//li/div/div[2]/div[2]/div/span/text()").extract()
            except:pass
            items.append(item)
        return items