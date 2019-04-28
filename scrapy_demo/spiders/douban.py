# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from ..items import DoubanListItem
import re

class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['douban.com']
    start_urls = ['https://www.douban.com/doulist/493021']

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
            info_lst = movie.css('.abstract::text').extract()
            info_dic = dict()
            # 去掉空格和换行符信息
            for i in range(len(info_lst)):
                info_one = info_lst[i].strip().replace('\n', '')
                reg = re.search('(.*?): (.*?$)', info_one, re.S)
                key_name = reg.group(1).encode('utf-8')
                key_val = reg.group(2)
                info_dic[key_name] = key_val
                print(reg.group(1))
            item['name'] = title
            item['img_url'] = img_url
            item['director'] = info_dic['导演'.decode('utf-8')]
            item['area'] = info_dic['制片国家/地区'.decode('utf-8')]
            item['year'] = info_dic['年份'.decode('utf-8')]

        # 检查有没有下一页 有的话 继续查找
        next_url = response.css('.next a::attr(href)').extract_first("")
        if next_url:
            yield Request(url=next_url, callback=self.parse)
