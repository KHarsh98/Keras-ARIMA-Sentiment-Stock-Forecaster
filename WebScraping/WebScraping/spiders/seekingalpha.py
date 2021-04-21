# -*- coding: utf-8 -*-
import scrapy


# TODO : IMPLEMENT NEXT PAGE PAGINATION FOLLOW


class SeekingalphaSpider(scrapy.Spider):
    name = 'seekingalpha'
    allowed_domains = ['seekingalpha.com']
    start_urls = ['https://seekingalpha.com/market-news/all']  # COULD DO : add more start urls for the website

    def parse(self, response):
        urls = response.css("div.title>a::attr(href)").extract()

        for url in urls:
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse_details)


        #Follow Next Page
        next_page_url = response.css('li.next>a::attr(href)').extract_first()
        if next_page_url:
            next_page_url = response.urljoin(next_page_url)
            yield scrapy.Request(url=next_page_url, callback=self.parse)

    def parse_details(self, response):
        titlep = response.css('h1::text').extract_first()
        datep = response.css("div.mc-info>time::text").extract()
        points = response.css("p.bullets_li").extract()

        for point in points:
            points[0] = points[0] + point

        text = points[0]

        yield {

            'title': titlep,
            'date': datep,
            'content': text

        }
