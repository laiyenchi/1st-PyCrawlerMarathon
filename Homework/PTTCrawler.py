# -*- coding: utf-8 -*-
import scrapy


class PttcrawlerSpider(scrapy.Spider):
    name = 'PTTCrawler'
    allowed_domains = ['https://www.ptt.cc/bbs/Gossiping/M.1581775326.A.E4D.html']
    start_urls = ['http://https://www.ptt.cc/bbs/Gossiping/M.1581775326.A.E4D.html/']

    def start_requests(self):
        for url in self.start_urls:            
            yield scrapy.Request(url, method='Get', callback=self.parse, cookies={'over18': '1'})



    def parse(self, response):
        pass
