import scrapy
from .. items import AmazonFinaldataItem

class AmazonSpider(scrapy.Spider):
    name = "amazonfinal"
    start_urls = [
        'https://www.amazon.com/Books-Last-30-days/s?rh=n%3A283155%2Cp_n_publication_date%3A1250226011',
    ]
    def parse(self, response):
        items = AmazonFinaldataItem()

        product_name = response.css('.a-color-base.a-text-normal').css('::text').extract()
        product_author = response.css('.sg-col-12-of-28 .a-size-base+ .a-size-base').css('::text').extract()
        product_price = response.css('.a-spacing-top-small .a-price span span').css('::text').extract()
        product_imagelink = response.css(".s-image::attr('src')").extract()

        # product_name = response.css('.a-color-base.a-text-normal::text').extract()
        # product_author = response.css('.sg-col-12-of-28 .a-size-base+ .a-size-base::text').extract()
        # product_price = response.css('.a-spacing-top-small .a-price span span::text').extract()
        # product_imagelink = response.css(".s-image::attr('src')").extract()

        items['product_name'] = product_name
        items['product_author'] = product_author
        items['product_price'] = product_price
        items['product_imagelink'] = product_imagelink

        yield items

        # next_page = response.css('li.next a::attr(href)').get()
        # print('Next page:', next_page)

        # if next_page is not None:
        #     yield response.follow(next_page, callback=self.parse)