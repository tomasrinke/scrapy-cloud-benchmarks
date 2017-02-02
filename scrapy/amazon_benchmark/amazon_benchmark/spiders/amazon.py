# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class AmazonSpider(CrawlSpider):
    name = 'amazon'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/']

    rules = (
        Rule(LinkExtractor(allow=r'/dp/'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        # from scrapy.shell import inspect_response
        # inspect_response(response, self)
        try:
            i = {}
            i['name'] = response.xpath('//meta[@name="title"]/@content').extract_first()
            i['id'] = response.xpath('//input[@id="ASIN"]/@value').extract_first()
            i['url'] = response.xpath('//link[@rel="canonical"]/@href').extract_first()
            i['price'] = response.xpath('//span[@id="priceblock_ourprice"]/text()').extract_first()
            return i
        except AttributeError:
            pass
