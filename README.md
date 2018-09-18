# scrapy-dynamodb
Dynamo DB pipeline for Scrapy.

## Installation

    python setup.py install

## Usage

Add below  to settings.py at your scrapy project.

    # settings.py

    ITEM_PIPELINES = {
        'dynamodbPipelines.DynamoDBPipeline': 300,
    }

    AWS_ACCESS_KEY_ID = '<aws access key id>'
    AWS_SECRET_ACCESS_KEY = '<aws secret access key>'
    DYNAMODB_REGION_NAME = '<dynamodb region name>'
    DYNAMODB_TABLE_NAME = '<my table name>'
    DYNAMODB_ENDPOINT_URL = 'http://localhost:8000'


 + variables description
   + DYNAMODB_PIPELINE_TABLE_NAME
       + table name, preexisted dynamodb table
   + DYNAMODB_ENDPOINT_URL
       + endpoint url (For Dynamo DB local, Optional !)

