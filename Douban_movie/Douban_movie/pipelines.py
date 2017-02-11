# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.conf import settings
import pymongo


class DoubanMoviePipeline(object):
    def __init__(self):
        host = settings['MOGGODB_HOST']
        port = settings['MOGGODB_PORT']
        dbName = settings['MOGGODB_DBNAME']
        client = pymongo.MongoClient(host=host, port=port)
        tdb = client[dbName]
        self.post = tdb[settings['MOGGODB_DOCNAME']]

    def process_item(self, item, spider):
        gameinfo = dict(item)
        self.post.insert(gameinfo)
        return item