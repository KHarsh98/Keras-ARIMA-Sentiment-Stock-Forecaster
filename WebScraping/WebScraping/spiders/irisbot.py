# -*- coding: utf-8 -*-
import scrapy


class IrisbotSpider(scrapy.Spider):
    name = 'irisbot'
    allowed_domains = ['ds.iris.edu/seismon/']
    start_urls = ['http://ds.iris.edu/seismon/eventlist/index.phtml']

    def parse(self, response):
        dates = response.xpath('//tr//td[1]//text()').extract()
        latlon = response.css('tr>td.latlon::text').extract()
        lat = latlon[::2]
        lon = latlon[1::2]

        mags =response.css('tr>td.mag::text').extract()
        depth = response.css('tr>td.dep::text').extract()

        for item in (dates, lat, lon, mags, depth):
            scraped_info = {
                'date' : item[0],
                'latitude' : item[1],
                'longitude' : item[2],
                'magnitude' : item[3],
                'depth' : item[4]
            }
            yield scraped_info


