import scrapy
import pandas as pd
from collector.items import CollectorItem



class CollectorSpider(scrapy.Spider):
    name = "collector"

    allowed_domains = ['theguardian.com']
    start_urls = ['https://www.theguardian.com/']

    def clean(self, string):
        encoded = string.encode('utf8')
        cleaned = encoded.strip()
        return cleaned

    def clean_list(self, list):
        for x in list:
            x = x.encode('utf8')


    def extract_authors(self, authors_list):
        authors = []
        for author in authors_list:
            cleanded = self.clean(author)
            name = cleanded.split('/')[-1]
            authors.append(name)
        return authors


    def start_requests(self):
        yield scrapy.Request(url='https://www.theguardian.com/', callback=self.parse)


    def parse(self, response):
        media_links = response.selector.xpath('//a[@data-link-name="article"] //@href').extract()

        for media_link in media_links :
            link = self.clean(media_link)
            yield scrapy.Request(url=link, callback=self.collect_content)

    def collect_content(self, response):
        media_content = response.xpath('//html')

        title = media_content.xpath('//meta[@property="og:title"] /@content').extract_first()
        authors = media_content.xpath("//meta[@property='article:author']/@content").extract()
        link = media_content.xpath("//meta[@property='og:url']/@content").extract()
        publish_time = media_content.xpath("//meta[@property='article:published_time']/@content").extract()
        description = media_content.xpath("//meta[@property='og:description']/@content").extract()


        media = CollectorItem()

        media['title'] = self.clean(title)
        media['author'] = self.extract_authors(authors)
        media['link'] = self.clean(link[0]) 
        media['publish_time'] = self.clean(publish_time[0])
        media['description'] = self.clean(description[0])
        yield media
