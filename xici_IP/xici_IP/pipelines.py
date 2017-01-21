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
# from .settings import DBKWARGS
class XiciSqlitePipline(object):
    def parse_item(self,item,spider):
        DBKWARGS = spider.seettings.get('DBKWARGS')
        con = pymysql.connect(**DBKWARGS)
        cur = con.curson()
        sql = ("insert into proxy(IP,PROT,IPTYPE,IPPOSITION,SPEED,LAST_CHECK_TIME) "
               "VALUES (%s,%s,%s,%s,%s,%s)")
        lis = (item['IP'],item['SPEED'],item['PROT'],item['IPTYPE'],item['IPPOSITION'],
                item['LAST_CHECK_TIME'])
        try:
            cur.execute(sql,lis)
        except Exception as e:
            print("Insert error:",e)
            con.rollback()
        else:
            con.comit()
        cur.close()
        con.close()
        return item



