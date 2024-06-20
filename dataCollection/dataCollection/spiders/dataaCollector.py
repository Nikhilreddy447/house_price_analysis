import scrapy


class DataacollectorSpider(scrapy.Spider):
    name = "dataaCollector"
    allowed_domains = ["magicbricks.com"]
    start_urls = ["https://magicbricks.com"]

    def parse(self, response):
        pass
