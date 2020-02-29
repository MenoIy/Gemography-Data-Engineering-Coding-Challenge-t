import scrapy

URL = "https://www.bbc.com"

class CollectorSpider(scrapy.Spider):
    name = "collector"

    def start_requests(self):
        yield scrapy.Request(url=URL, callback=self.parse)

    def parse(self, response):
        filename = 'collected.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)