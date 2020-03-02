# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class CollectorPipeline(object):
    def process_item(self, item, spider):
        return item




import pymongo

from scrapy import settings
from scrapy.exceptions import DropItem


class MongoDBPipeline(object):

    def __init__(self):
        #mongodb connection
        client = pymongo.MongoClient("mongodb+srv://menoly:sakata-1@cluster0-ehtfy.gcp.mongodb.net/test?retryWrites=true&w=majority")
        
        #drop the collection
        client.drop_database('theguardian')

        #create new collection
        db = client['theguardian']
        self.client = db['news']

    def process_item(self, item, spider):
        '''inserting item to database'''
        self.client.insert(dict(item))
        return item