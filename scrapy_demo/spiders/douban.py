# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://www.douban.com/doulist/73124']

    def parse(self, response):
        movies = response.css('.doulist-item')

        with open('./movies.txt', 'wb') as f:
            for movie in movies:
                title = movie.css('.title a::text').extract()[1]

                title = title.strip().replace('\n', '')
                print(title)

                f.write(title)
