# web-crawling-basic

# Install
First install Scrapy in your virtual environment.
pip3 install Scrapy

# Creater a project
First active your environment the run the folowing command.
scrapy startproject projectname

We will work on spiders folder.
And working on http://quotes.toscrape.com/ url for practice.

# Run the crealer
To run the clowler you need to run the following command-
scrapy crawl spidername

# Types of data crawling
We can crawling mainly 2 ways.
1.CSS
2.Xpath

We can test crawling in console.
For testing in console please run the following code-
scrapy shell "your path"

you can read data using both way
response.css('title::text').extract()
or,
response.xpath('//title/text()').extract()

For css you targeting class or id-
response.css('title.className::text').extract()
response.css('title#idName::text').extract()

For xpath you targeting class or id-
response.xpath('//title[@class='text']/text()').extract()
response.xpath('//title[@id='text']/text()').extract()

We can use both together-
response.css('li.next a').xpath('@href').extract()

Get href url-
using css-
response.css('li.next a::attr(href)').extract()
or,
response.css('li.next a::attr(href)').get()
This will get single value. Use this when you want get single value.

We can use more .css in query-
product_name = response.css('.a-color-base.a-text-normal').css('::text').extract()

using xpath-
response.xpath("//li[@class='next']/a/@href").extract()

# Storing in JSON, XML and CSV
scrapy crawl quotes -o items.json
scrapy crawl quotes -o items.xml
scrapy crawl quotes -o items.csv

# Storeing data in database
We need use pipeleine for pasiing data to database.
It's a structured way...
First go to settings.py and uncomment the pipeline.

# Next page (pagination)
you can paginate your crwaler.
Add the flowing code-
next_page = response.css('li.next a::attr(href)').get()
        print('Next page:', next_page)

if next_page is not None:
    yield response.follow(next_page, callback=self.parse)

# Bypass Restrictions
Some web are restricted for crawling a lots of data.
To solve this problem we can use user agent or proxy.


# User agent
For that reason you need to add the user agent in your settings.py file
I am using google bot user agent.
or you can use others library scrapy users agent.
For scrapy user agent you need to install the library-
pip3 install scrapy-user-agents

Then you need add middleware in our settings file.
DOWNLOADER_MIDDLEWARES = {
    'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware': None,
    'scrapy_user_agents.middlewares.RandomUserAgentMiddleware': 400,
}

# Proxy
Enable this middleware by adding the following settings to your settings.py:

PROXY_POOL_ENABLED = True
Then add rotating_proxies middlewares to your DOWNLOADER_MIDDLEWARES:

DOWNLOADER_MIDDLEWARES = {
    # ...
    'scrapy_proxy_pool.middlewares.ProxyPoolMiddleware': 610,
    'scrapy_proxy_pool.middlewares.BanDetectionMiddleware': 620,
    # ...
}
