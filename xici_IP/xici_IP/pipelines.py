# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import pymysql
# import json
# import codecs
# class XiciIpPipeline(object):
#     def __init__(self):
#         self.file = codecs.open('item.jl','wb',encoding='UTF-8')
#     def process_item(self, item, spider):
#         line = json.dumps(dict(item),ensure_ascii=False) + '\n'
#         self.file.write(line)
#         return item
#     def spider_closed(self, spider):
#         self.file.close()
# from twisted.enterprise import adbapi
import pymysql
class CollectipsPipeline(object):

    def process_item(self, item, spider):

        DBKWARGS = spider.settings.get('DBKWARGS')
        con = pymysql.connect(**DBKWARGS)
        cur = con.cursor()
        sql = ("insert into proxy(IP,PORT,IPTYPE,IPPOSITION,SPEED,LAST_CHECK_TIME) "
            "values(%s,%s,%s,%s,%s,%s)")
        lis = (item['IP'],item['PORT'],item['IPTYPE'],item['IPPOSITION'],item['SPEED'],
            item['LAST_CHECK_TIME'])
        try:
            cur.execute(sql,lis)
        except Exception as e:
            print("Insert error:",e)
            con.rollback()
        else:
            con.commit()
        cur.close()
        con.close()
        return item

