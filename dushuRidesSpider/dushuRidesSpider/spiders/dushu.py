import scrapy
from scrapy_redis.spiders import RedisSpider
from dushuRidesSpider.items import DushuridesspiderItem


class DushuSpider(RedisSpider):
    name = 'dushu'
    allowed_domains = ['www.dushu.com']
    # start_urls = ['https://www.dushu.com/lianzai/1115_1.html']
    redis_key = 'start_urls'

    def parse(self, response):
        bookslist = response.css('.bookslist h3 > a::attr(href)').getall()
        if len(bookslist) == 0:
            return
        for booksUrl in bookslist:
            yield response.follow(url=booksUrl, callback=self.bookParse)

        nextUrl = response.css('a:contains(下一页)::attr(href)').get(default='')
        yield response.follow(url=nextUrl, callback=self.parse)

    def bookParse(self, response):
        item = DushuridesspiderItem()
        book_name = response.css('.book-title > h1::text').get()
        author = response.css('tbody > tr > td::text').getall()[1]
        text = response.css('.text.txtsummary::text').get()
        item['name'] = book_name
        item['author'] = author
        item['text'] = text

        yield item
