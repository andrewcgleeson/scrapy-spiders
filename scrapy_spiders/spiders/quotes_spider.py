import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.xpath('//div[contains(@class, "quote")]'):
            yield {
                'text': quote.xpath('span/text()').get(),
                'author': quote.xpath('span/small[contains(@class, "author")]/text()').get(),
                'tags': quote.xpath('div[contains(@class, "tags")]/a[contains(@class, "tag")]/text()').getall(),
            }

        next_page = response.xpath('//li[contains(@class, "next")]/a/@href').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)