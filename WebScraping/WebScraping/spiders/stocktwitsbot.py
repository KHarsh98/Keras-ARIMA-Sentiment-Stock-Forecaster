# -*- coding: utf-8 -*-
import scrapy


class StocktwitsbotSpider(scrapy.Spider):
    name = 'stocktwitsbot'
    allowed_domains = ['stocktwits.com']
    start_urls = ['http://stocktwits.com/']

    def parse(self, response):
        pass
