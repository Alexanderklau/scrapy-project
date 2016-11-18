# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from urllib.request import urlopen

class PrettylegsPipeline(object):
    def process_item(self, item, spider):
        IMAGE_STORE = '/home/lau/PycharmProjects/scrapy-spider-project/prettylegs/prettylegImage'
        dir_path = '%s/%s' % (IMAGE_STORE,spider.name)
        print('dir_path',dir_path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
        for image_url in item['imageUrl']:
            list_name = image_url.split('/')
            file_name = list_name[len(list_name) - 1]
            file_path = '%s/%s' %(dir_path,file_name)
            if os.path.exists(file_name):
                continue
            with open(file_path,'wb') as file_writer:
                conn = urlopen(image_url)
                file_writer.write(conn.read())
            file_writer.close()
        return item
