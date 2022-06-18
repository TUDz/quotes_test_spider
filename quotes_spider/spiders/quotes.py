import scrapy
from quotes_spider.items import QuotesSpiderItem
from scrapy.loader import ItemLoader

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.xpath('//*[@class="quote"]')
        for quote in quotes:
            l = ItemLoader(item=QuotesSpiderItem(), response=response)
            text = quote.xpath('.//*[@class="text"]/text()').extract_first()
            author = quote.xpath('.//*[@class="author"]/text()').extract_first()
            tags = quote.xpath('.//*[@class="tags"]/a/text()').extract()
            
            l.add_value('text', text)
            l.add_value('author', author)
            l.add_value('tags', tags)
            yield l.load_item()
            
        next_page_url = response.xpath('//li[@class="next"]/a/@href').extract_first()
        absolute_next_page_url = response.urljoin(next_page_url)
        yield scrapy.Request(absolute_next_page_url)