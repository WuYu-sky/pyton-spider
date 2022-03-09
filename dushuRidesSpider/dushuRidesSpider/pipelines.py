# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json

from itemadapter import ItemAdapter


# class DushuridesspiderPipeline:
#     def process_item(self, item, spider):
#
#         return item


import pymongo
import redis


class MongoPipeline:
    collection_name = 'use'

    def __init__(self, mongo_url, mongo_db):
        self.mongo_url = mongo_url
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_url=crawler.settings.get('MONGO_URL'),
            mongo_db=crawler.settings.get('MONGO_DATABASE')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_url)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert_one(ItemAdapter(item).asdict())
        return item


class MyRedisPipeline:
    def __init__(self):
        self.redis_cli = redis.StrictRedis(
            host='redis服务器地址', port=6379, db=0, password='redis密码'
        )

    def process_item(self, item, spider):
        # self.redis_cli.lpush('name', item['name'], item['author'], item['text'])
        self.redis_cli.lpush('text', json.dumps(dict(item)))
        return item
