import scrapy
import pandas as pd

URL = "https://www.bbc.com/"




def clean(string):
    value = string.encode('utf8')
    value = value.strip()
    return value


class CollectorSpider(scrapy.Spider):
    name = "collector"

    def start_requests(self):
        yield scrapy.Request(url=URL, callback=self.parse)


    def parse(self, response):
        
        contents_list = []
        
        media_contents = response.css('div.media__content')
        for media_content in media_contents:
            content = {}

            media_title = media_content.css('h3.media__title')
            title = media_title.xpath('a//text()').extract()
            if title :
                content['title'] = clean(title[0])

            href = media_title.xpath('a//@href').extract()
            if href :
                content['href'] = clean(href[0])

            tag = media_content.xpath('a//text()').extract()
            if tag:
                content['tag'] = clean(tag[0])

            summary = media_content.xpath('p//text()').extract()
            if summary:
                content['summary'] = clean(summary[0])
             
            contents_list.append(content)
        
        df = pd.DataFrame(contents_list)
        df.to_csv('./bbc.csv', index=False)
            
         