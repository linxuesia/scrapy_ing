# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from ..items import DoubanListItem


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://www.douban.com/doulist/706287']

    def parse(self, response):
        movies = response.css('.doulist-item')

        # 获取豆列的名字 写入txt文件中
        # headline = response.css('h1::text').extract_first("")
        # file_path = './%s.txt' % headline
        # with open(file_path, 'a', encoding='utf-8') as f:
        #     for movie in movies:
        #         lst = movie.css('.title a::text').extract()
        #         if len(lst) > 1:
        #             title = lst[1]
        #         else:
        #             title = lst[0]
        #         f.write(title)

        # 获取到相关信息 存入item
        item = DoubanListItem()
        for movie in movies:
            # 获取标题
            lst = movie.css('.title a::text').extract()
            if len(lst) > 1:
                title = lst[1]
            else:
                title = lst[0]
            title = title.strip().replace('\n', '')
            # 获取图片地址
            img_url = movie.css('.post img::attr(href)').extract()
            # 获取详情
            info = movie.css('.abstract::text').extract()
            for i in len(info):
                info[i] = info[i].strip().replace('\n', '')
            print(info)
            item['name'] = title
            item['img_url'] = img_url

        # 检查有没有下一页 有的话 继续查找
        next_url = response.css('.next a::attr(href)').extract_first("")
        if next_url:
            yield Request(url=next_url, callback=self.parse)
