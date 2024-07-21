import scrapy


class QuotesToscrapeSpider(scrapy.Spider):
    name = "quotes_toscrape"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com/"]

    max_depth = 1

    def parse(self, response):
        quotes = response.xpath('//div[@class="quote"]')
        
        for quote in quotes:
            text = quote.xpath('.//span[@class="text"]/text()').get()
            author = quote.xpath('.//small[@class="author"]/text()').get()

            yield {
                'text': text,
                'author': author
            }

        next_button = response.xpath('//li[@class="next"]/a/@href').get()

        if next_button and self.max_depth:
            self.max_depth -= 1
            yield response.follow(next_button, callback=self.parse)
