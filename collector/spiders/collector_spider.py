import scrapy
import re
from collector.items import CollectorItem



class CollectorSpider(scrapy.Spider):
    name = "collector"

    allowed_domains = ['theguardian.com']
    start_urls = ['https://www.theguardian.com/']


    def start_requests(self):
        yield scrapy.Request(url='https://www.theguardian.com/', callback=self.parse)


    def parse(self, response):
        media_links = response.selector.xpath('//a[@data-link-name="article"] //@href').extract()
        # media_links list of all article links in the response.url
        for media_link in media_links :
            # getting articl info from every link
            yield scrapy.Request(url=media_link, callback=self.collect_content)

    def collect_content(self, response):
        media_content = response.xpath('//html')

        # this is group of raw info:
        title = media_content.xpath('//meta[@property="og:title"] /@content').extract_first()
        authors = media_content.xpath("//meta[@property='article:author']/@content").extract()
        link = media_content.xpath("//meta[@property='og:url']/@content").extract()
        publish_time = media_content.xpath("//meta[@property='article:published_time']/@content").extract()
        description = media_content.xpath("//meta[@property='og:description']/@content").extract()
        keywords = media_content.xpath("//meta[@name='keywords']/@content").extract()

        # this is not articles : 
        raw_articles = media_content.xpath('//div[@itemprop="articleBody"]//p').extract()

        # cleaning and storing raw info in item
        media = CollectorItem()

        media['title'] = title
        media['author'] = [author.split('/')[-1] for author in authors]
        media['link'] = link[0]
        media['publish_time'] = publish_time[0].replace('T', ' ')[:-5]
        media['description'] = description[0]
        media['keywords'] = [word for keyword in keywords for word in keyword.split(",")]

        #cleaning articles 
        cleaner =  re.compile('<.*?>')
        articles = ""
        for raw_article in raw_articles:
            if raw_article != '\n':
                articles += raw_article
        
        media['articles'] = re.sub(cleaner, '', articles)
        yield media
