import scrapy
from ..items import JobdataItem
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
class findjobSpider(scrapy.Spider):
    name = 'job'
    allowed_domains = ['lagou.com']
    start_urls = ['https://www.lagou.com/zhaopin/Java/1/']

    rules = (
        Rule(LinkExtractor(allow=r'/\d/$'), callback='parse_item', follow=True),

    )

    def parse(self, response):
        items = []
        job_list = response.xpath("/html/body/div[2]/div[2]/div[1]/div[3]/ul")
        for job in job_list:
            item = JobdataItem()
            try:
                item['company_name'] = job.xpath("//li/div[1]/div[2]/div[1]/a/text()").extract()
                item['company_reward'] = job.xpath("//li/div[1]/div[1]/div[2]/div/span/text()").extract()
                item['company_require'] = job.xpath("//li/div[1]/div[1]/div[1]/a/h2/text()").extract()
                item['company_type'] = job.xpath("//li/div[1]/div[2]/div[2]/text()").extract()
                item['company_introduce'] = job.xpath("//li/div[2]/div[2]/text()").extract()
            except:
                pass
            items.append(item)
        return items