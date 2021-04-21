# -*- coding: utf-8 -*-
import scrapy


class QuoteswsjbotSpider(scrapy.Spider):
    name = 'quoteswsjbot'
    allowed_domains = ['quotes.wsj.com']
    start_urls = ['https://quotes.wsj.com/AMZN?mod=searchresults_companyquotes']

    def parse(self, response):
        headline = response.css(".headline>a::text").extract()
        date

