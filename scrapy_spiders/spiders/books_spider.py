import scrapy

class BooksSpider(scrapy.Spider):
    name = "books"
    start_urls = [
        'http://books.toscrape.com/',
    ]

    def parse(self, response):
        for book in response.xpath('//ol[contains(@class, "row")]'):
            yield {
                'name': book.xpath('//h3/a/text()').get(),
                'rating': book.xpath('//p/@class').get(),
                'price': book.xpath('//div[contains(@class, "product_price")]/p[contains(@class, "price_color")]/text()').get(),
            }

        next_page = response.xpath('//li[contains(@class, "next")]/a/@href').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)