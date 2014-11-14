# -*- coding: utf-8 -*-
import scrapy
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
import re
from items import ImageItem


class MmspiderSpider(CrawlSpider):
    name = 'mmspider'
    allowed_domains = ['22mm.cc']
    start_urls = ['http://www.22mm.cc/']
    rules = (
        Rule(
            LinkExtractor(
                allow=('\w+(\-\d+)?\.html', ), ),
            callback='image_links',
            follow=True)
            )

    def image_links(self, response):
        imageItem = ImageItem()
        url_list = response.xpath('//div[@id="imgString"]/../script').re(r'http.*?jpg')
        img_urls = [re.sub(r'(?<=meimei22\.com)/.*?/','/pic/',url) for url in url_list]
        if img_urls: return ImageItem(image_urls=img_urls)
