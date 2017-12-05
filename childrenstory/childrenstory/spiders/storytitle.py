from scrapy.spiders import Spider
from scrapy.http import Request
from scrapy.selector import Selector
from childrenstory.items import StorytitleItem

class StorytitleSpider(Spider):
    name = 'storytitle'

    download_delay = 1
    allowed_domains = ['www.ximalaya.com']
    start_urls = ['http://www.ximalaya.com/dq/kid']

    def parse(self, response):
        sel = Selector(response)
        item = StorytitleItem()

        story_url = str(response.url)
        story_name = sel.xpath('//div[@id="explore_album_detail_entry"]/div[@class="discoverAlbum_wrapper"]/div[@class="discoverAlbum_item"]/a/text()').extract()

        item['story_name'] = [n.encode('utf-8') for n in story_name]
        item['story_url'] = story_url.encode('utf-8')

        yield item

        urls = sel.xpath('//div[@class="pagingBar_wrapper"]/a[@rel="next"]/@href').extract()
        for url in urls:
            print url
            url = "http://ximalaya.com" + url
            print url
            yield Request(url, callback=self.parse,dont_filter = True)
