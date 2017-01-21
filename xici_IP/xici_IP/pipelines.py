# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import json
import codecs
class XiciIpPipeline(object):
    def __init__(self):
        self.file = codecs.open('item.jl','wb',encoding='UTF-8')
    def process_item(self, item, spider):
        line = json.dumps(dict(item),ensure_ascii=False) + '\n'
        self.file.write(line)
        return item
    def spider_closed(self, spider):
        self.file.close()
from twisted.enterprise import adbapi
import pymysql
import pymysql.cursors
class XiciSqlitePipline(object):
    def __init__(self):
        dbargs = dict(
            host = '127.0.0.1'
        )
