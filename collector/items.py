# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field


class CollectorItem(scrapy.Item):
    title = Field()
    article = Field()
    author = Field()
    description = Field()
    publish_time = Field()
    link = Field()
    keywords = Field()
    pass
