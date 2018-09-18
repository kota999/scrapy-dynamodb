# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    name='scrapy-dynamodb',
    version='0.0.1',
    description='Dynamo DB pipeline for Scrapy',
    long_description=open('README.md').read(),
    author='kota999',
    author_email='kota99949@gmail.com',
    url='https://github.com/kota999/scrapy-dynamedb',
    license=open('LICENSE').read(),
    install_requires=['boto3'],
    packages=find_packages()
)
