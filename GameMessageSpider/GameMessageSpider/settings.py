# -*- coding: utf-8 -*-

BOT_NAME = 'GameMessageSpider'

SPIDER_MODULES = ['GameMessageSpider.spiders']
NEWSPIDER_MODULE = 'GameMessageSpider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64; rv:45.0) Gecko/20100101 Firefox/45.0'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
   'GamesMessageSpider.pipelines.GamemessagespiderPipeline': 300,
}
COOKIES_ENABLED = True
DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Language': 'en-US,en;q=0.5',}
MOGGODB_HOST = '127.0.0.1'
MOGGODB_PORT = 27017
MOGGODB_DBNAME = 'Game'
MOGGODB_DOCNAME = 'game_message'


