import scrapy
from scrapy.selector import Selector
import json
from ..items import DoubanMovieItem


class Douban_Spider(scrapy.Spider):
    name = 'Movie'
    start_urls = []
    for temp in range(0,250,25):
        url = 'https://movie.douban.com/top250?start=' + str(temp)
        start_urls.append(url)

    def parse(self, response):
        sel = Selector(response)
        movies = sel.xpath('//html/body/div[3]/div[1]/div/div[1]/ol')
        for movie in movies:
            item = DoubanMovieItem()
            item['name'] = movie.xpath('//li/div/div[2]/div[1]/a/span[1]/text()').extract()
            item['star'] = movie.xpath('//li/div/div[2]/div[2]/div/span[2]/text()').extract()
            item['introduction'] = movie.xpath('//li/div/div[2]/div[2]/p[2]/span/text()').extract()
            yield item



