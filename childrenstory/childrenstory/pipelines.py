# -*- coding: utf-8 -*-

# Define your item pipelines here
# -*- coding: utf-8 -*-
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import codecs

import urllib
import os
from childrenstory import settings

import pymongo
from scrapy.conf import settings

class StorytitlePipeline(object):
    def __init__(self):
        self.file = codecs.open('story_title_data.json',mode='wb',encoding='utf-8')

    def process_item(self, item, spider):
        line = json.dumps(dict(item)) + '\n'
        self.file.write(line.decode("unicode_escape"))

        return item

class Storymp3Pipeline(object):
    def __init__(self):
        self.file = codecs.open('story_mp3_data.json',mode='wb',encoding='utf-8')

    def process_item(self,item,spider):
        line = json.dumps(dict(item)) + '\n'
        self.file.write(line.decode("unicode_escape"))

        return item

    def spider_closed(self,spider):
        self.file.close()

class XimalayaMongoPipeline(object):
    def __init__(self):
        host = settings['MONGODB_HOST']
        port = settings['MONGODB_PORT']
        dbname = settings['MONGODB_NAME']
        clint = pymongo.MongoClient()  # 本地可以不加东西也行
        tdb = clint[dbname]  # 通过这种方式选择数据库名
        self.post = tdb[settings['MONGODB_TABLE']]

    def process_item(self,item,spider):
        postItem = dict(item)  # 把item转化成字典形式
        self.post.insert(postItem)  # 向数据库插入一条记录
        return item  # 会在控制台输出原item数据，可以选择不写

class StoryimgPipeline(object):
     def process_item(self, item, spider):
         #存储路径
        dir_path = '%s/%s' %(settings.IMAGES_STORE,spider.name)
        # print 'dir_path',dir_path
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        for story_imgurl in item['story_imgurls']:
            list_name = story_imgurl.split('/')
            # print 'list_name',list_name
            list_names = list_name[len(list_name)-1].split('?')
            #图片命名
            file_name = list_names[0]
            # print 'filename',file_name
            file_path = '%s/%s' %(dir_path,file_name)
            # print 'file_path',file_path
            if os.path.exists(file_name):
                continue
            with open(file_path,'wb') as file_writer:
                #下载图片
                conn = urllib.urlopen(story_imgurl)
                file_writer.write(conn.read())
            file_writer.close()
        return item
