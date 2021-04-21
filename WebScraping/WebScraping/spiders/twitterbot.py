# -*- coding: utf-8 -*-
import scrapy


class TwitterbotSpider(scrapy.Spider):
    name = 'twitterbot'
    allowed_domains = ['twitter.com/']
    start_urls = ['https://twitter.com/search?q=amazon%20stock%20price%20since%3A2016-01-01%20until%3A2018-01-01&src=typd//']

    def parse(self, response):
        pass

