import scrapy
import pandas as pd
from collector.items import CollectorItem



class CollectorSpider(scrapy.Spider):
    name = "collector"

    allowed_domains = ['theguardian.com']
    start_urls = ['https://www.theguardian.com/']


    def start_requests(self):
        yield scrapy.Request(url='https://www.theguardian.com/', callback=self.parse)


    def parse(self, response):
        media_links = response.selector.xpath('//a[@data-link-name="article"] //@href').extract()

        for media_link in media_links :
            yield scrapy.Request(url=media_link, callback=self.collect_content)

    def collect_content(self, response):
        media_content = response.xpath('//html')

        title = media_content.xpath('//meta[@property="og:title"] /@content').extract_first()
        authors = media_content.xpath("//meta[@property='article:author']/@content").extract()
        link = media_content.xpath("//meta[@property='og:url']/@content").extract()
        publish_time = media_content.xpath("//meta[@property='article:published_time']/@content").extract()
        description = media_content.xpath("//meta[@property='og:description']/@content").extract()
        keywords = media_content.xpath("//meta[@name='keywords']/@content").extract()


        media = CollectorItem()

        media['title'] = title
        media['author'] = [author.split('/')[-1] for author in authors]
        media['link'] = link[0]
        media['publish_time'] = publish_time[0]
        media['description'] = description[0]
        media['keywords'] = [word for keyword in keywords for word in keyword.split(",")]
        yield media
