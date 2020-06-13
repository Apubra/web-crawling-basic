import scrapy
from .. items import AmazondataItem
class AmazonSpider(scrapy.Spider):
    name = "amazonspider"
    start_urls = [
        'http://quotes.toscrape.com/',
    ]

    # Practice 1
    # def parse(self, response):
    #     title = response.css('title::text').extract()
    #     yield{'titletetext': title}

    # Practice 2
    def parse(self, response):
        items = AmazondataItem()
        all_div_quotes = response.css('div.quote')
        
        for quotes in all_div_quotes:
            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tag::text').extract()

            items['title'] = title
            items['author'] = author
            items['tag'] = tag

            # yield{'title': title, 'author':author, 'tag':tag}
            yield items

        next_page = response.css('li.next a::attr(href)').get()
        print('Next page:', next_page)

        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)