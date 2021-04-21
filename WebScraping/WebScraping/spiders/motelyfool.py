# -*- coding: utf-8 -*-
import scrapy
#TODO: GET infinite scroll to work

#TODO: Think about scraping some specific company by a search query on the website

#MOTELY SPIDER V2.0

class MotelyfoolSpider(scrapy.Spider):
    name = 'motelyfool'
    allowed_domains = ['www.fool.com']
    start_urls = ['https://www.fool.com/investing-news/?page=1']

    def parse(self, response):

        urls =response.css(".text>h4>a::attr(href)").extract()

        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback= self.parse_details)


    def parse_details(self, response):
        titlep = response.css('header>h1::text').extract_first()
        datep = response.css('.publication-date::text').extract_first()
        paragraphs = response.css('.article-content>p::text').extract()



        for para in paragraphs:
            paragraphs[0] = paragraphs[0] + para

        text = paragraphs[0]

        yield {
            'title': titlep,
            'date': datep,
            'content': text

            }

