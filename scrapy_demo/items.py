# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyDemoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class DoubanListItem(scrapy.Item):
    name = scrapy.Field()
    img_url = scrapy.Field()
    score = scrapy.Field()
    type = scrapy.Field()
    area = scrapy.Field()
    director = scrapy.Field()
    year = scrapy.Field()
