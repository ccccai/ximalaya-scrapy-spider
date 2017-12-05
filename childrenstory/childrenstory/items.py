# -*- coding: utf-8 -*-

# Define here the models for your scraped items
# -*- coding: utf-8 -*-
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#爬取故事名字
class StorytitleItem(scrapy.Item):
    story_name = scrapy.Field() #故事名称
    story_url = scrapy.Field() #故事链接
    pass

#爬取故事封面
class StoryimgItem(scrapy.Item):
    story_imgurls = scrapy.Field() #封面地址
    # story_imgs = scrapy.Field()
    # story_imgpath = scrapy.Field()
    pass

#爬取音频地址
class Storymp3Item(scrapy.Item):
    mp3_name = scrapy.Field()
    mp3_url = scrapy.Field()
    story_url = scrapy.Field()
    json_url = scrapy.Field()
    # mp3_ids = scrapy.Field()
    pass

class Pagemp3Item(scrapy.Item):
    album_name = scrapy.Field()
    album_url = scrapy.Field()
    album_imgurl = scrapy.Field()
    json_url = scrapy.Field()
    mp3_name = scrapy.Field()
    mp3_url = scrapy.Field()
