# -*- coding: utf-8 -*-
import scrapy

#TODO: figure out CSS of this site and how to select it


class YahoobotSpider(scrapy.Spider):
    name = 'yahoobot'
    allowed_domains = ['www.finance.yahoo.com/']
    start_urls = ['http://www.finance.yahoo.com//']

    def parse(self, response):
        pass



