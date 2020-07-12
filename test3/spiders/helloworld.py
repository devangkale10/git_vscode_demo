import scrapy
import sqlite3


class HelloworldSpider(scrapy.Spider):
    name = 'helloworld'
    allowed_domains = ['amazon.com']
    start_urls = ['http://facebook.com/']

    def parse(self, response):
