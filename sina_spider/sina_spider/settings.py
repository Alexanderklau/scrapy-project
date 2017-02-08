BOT_NAME = 'sina_spider'

SPIDER_MODULES = ['sina_spider.spiders']

NEWSPIDER_MODULE = 'sina_spider.spiders'

ROBOTSTXT_OBEY = True

SPIDER_MIDDLEWARES = {
   'sina_spider.middleware.userAgentMiddleware': 401,
}

