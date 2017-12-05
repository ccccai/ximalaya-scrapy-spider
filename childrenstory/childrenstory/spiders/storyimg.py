# -*- coding: utf-8 -*-
import scrapy
from scrapy.crawler import CrawlerProcess
from childrenstory.items import StoryimgItem
from scrapy.http import Request
from scrapy.selector import Selector

class StoryimgSpider(scrapy.Spider):
    name = 'storyimg'
    download_delay = 1
    allowed_domains = ["http://ximalaya.com"]
    start_urls = ["http://www.ximalaya.com/dq/kid"]

    def parse(self, response):
        sel = Selector(response)
        item = StoryimgItem()
        item['story_imgurls'] = response.xpath('//div[@id="explore_album_detail_entry"]/div[@class="discoverAlbum_wrapper"]/div[@class="discoverAlbum_item"]/div[@class="albumfaceOutter"]/a/span/img/@src').extract()#提取图片链接
        # print 'story_imgurls',item['story_imgurls']
        yield item

        urls = sel.xpath('//div[@class="pagingBar_wrapper"]/a[@rel="next"]/@href').extract()
        for url in urls:
            print url
            url = "http://ximalaya.com" + url
            print url
            yield Request(url, callback=self.parse,dont_filter = True)
