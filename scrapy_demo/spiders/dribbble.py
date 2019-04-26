# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from urllib import parse

class DribbbleSpider(scrapy.Spider):

    name = 'dribbble'
    allowed_domains = ['dribbble.com']
    start_urls = ['http://dribbble.com/stories']

    def parse(self, response):
        urls = response.css('h2 a::attr(href)').extract()

        for url in urls:
            yield Request(url=parse.urljoin(response.url, url), callback=self.parse_analyze)

        next_url = response.css('a.next_page::attr(href)').extract()[0]

        if next_url:
            yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)

    def parse_analyze(self, response):
        title = response.css('h1::text').extract_first()
        print(title)
