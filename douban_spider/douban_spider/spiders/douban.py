# -*- coding:utf-8 -*-

from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import Selector
from ..items import DoubanSpiderItem
#from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

from html.parser import HTMLParser as SgmlLinkExtractor
try:
    from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
except:
    from html.parser import HTMLParser as SgmlLinkExtractor


# import sys
# reload(sys)
# sys.setdefaultencoding('utf8')

class DoubanSpider(CrawlSpider) :

    name = "douban"
    allowed_domains = ["movie.douban.com"]
    start_urls = ["http://movie.douban.com/top250"]
    rules = (
        #将所有符合正则表达式的url加入到抓取列表中
        Rule(SgmlLinkExtractor(allow = (r'http://movie\.douban\.com/top250\?start=\d+&filter=&type=',))),
        #将所有符合正则表达式的url请求后下载网页代码, 形成response后调用自定义回调函数
        Rule(SgmlLinkExtractor(allow = (r'http://movie\.douban\.com/subject/\d+', )), callback = 'parse_page', follow = True),
        )

    def parse_page(self, response) :
        sel = Selector(response)
        item = DoubanSpider()
        item['name'] = sel.xpath('//h1/span[@property="v:itemreviewed"]/text()').extract()
        item['description'] = sel.xpath('//div/span[@property="v:summary"]/text()').extract()
        item['url'] = response.url
        return item