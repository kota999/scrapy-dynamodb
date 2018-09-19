# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import boto3


def default_encoder(value, empty_str_replacement = 'empty'):
    import datetime
    # For datetime
    if isinstance(value, datetime.datetime):
        return value.strftime('%Y-%m-%d %H:%M:%S')
    elif isinstance(value, datetime.date):
        return value.strftime('%Y-%m-%d')
    elif isinstance(value, datetime.time):
        return value.strftime('%H:%M:%S')
    else:
        # For empty str
        if isinstance(value, str):
            if value == '':
                value = empty_str_replacement
        return value


class DynamoDBPipeline(object):

    def __init__(self, crawler, encoder=default_encoder):
        self.encoder = encoder
        self.aws_access_key_id = crawler.settings['AWS_ACCESS_KEY_ID']
        self.aws_secret_access_key = crawler.settings['AWS_SECRET_ACCESS_KEY']
        self.region_name = crawler.settings['DYNAMODB_REGION_NAME']
        self.endpoint_url = crawler.settings['DYNAMODB_ENDPOINT_URL']
        self.table_name = crawler.settings['DYNAMODB_TABLE_NAME']
        self.table = None

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def open_spider(self, spider):
        db = boto3.resource(
            'dynamodb',
            aws_access_key_id=self.aws_access_key_id,
            aws_secret_access_key=self.aws_secret_access_key,
            region_name=self.region_name,
            endpoint_url=self.endpoint_url
        )
        self.table = db.Table(self.table_name)

    def close_spider(self, spider):
        self.table = None

    def process_item(self, item, spider):
        self.table.put_item(
            TableName=self.table_name,
            Item={k: self.encoder(v) for k, v in item.items()},
            # TODO: add condintion extension, example is below
            # ExpressionAttributeNames={"#name"  : "name",},
            # ConditionExpression='attribute_not_exists(#name) AND attribute_not_exists(category)',
        )
        return item
