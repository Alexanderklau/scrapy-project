#coding=utf-8
import imp,sys
imp.reload(sys)
#python默认环境编码时ascii
import os

#os.system(r"scrapy crawl douban")
#读取电影数据
movies_info = open('movies.sql','r')
try:
    for line in movies_info:
        #将每条电影数据里面的需要的数据提取出来
        movie_infos = line.split(',',4)

        movie_id = movie_infos[1]
        movie_title = movie_infos[2]
        #print movie_id + ":" + movie_title

        write_name = movie_title.replace('_','+')
        write_name = write_name.replace('\'','')
        #print "name is :" + write_name
        #把电影名写到中间文件中去，让爬虫读取
        movie_name_file = open('movie_name.txt','w')
        try:
            movie_name_file.write(write_name)
        finally:
            movie_name_file.close()
        #把电影id写到中间文件中去，让爬虫读取
        movie_id_file = open('movie_id.txt','w')
        try:
            movie_id_file.write(movie_id)
        finally:
            movie_id_file.close()

        #该爬虫程序会从movie_name中读取电影名来爬虫
        os.system(r"scrapy crawl douban")

finally:
    movies_info.close()