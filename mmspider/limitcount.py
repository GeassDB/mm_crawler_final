#encoding:utf8

from scrapy import signals,log
from scrapy.exceptions import NotConfigured
from twisted.internet import reactor

class LimitCountExtension(object):

    def __init__(self, item_count):
        self.item_count = item_count
        print(self.item_count)
        self.items_scraped = 0

    @classmethod
    def from_crawler(cls, crawler):
        item_count = crawler.settings.getint('MAX_DOWNLOAD_COUNT')
        print(item_count)
        if item_count<=0: raise NotConfigured

        ext = cls(item_count)

        crawler.signals.connect(ext.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(ext.item_scraped, signal=signals.item_scraped)

        return ext

    def spider_opened(self, spider):
        self.item_scraped = 0
        spider.log('spider opened.')

    def item_scraped(self, spider):
        self.items_scraped += 1
        log.msg('%d item(s) scraped.' % self.items_scraped)
        if self.items_scraped >= self.item_count:
            log.msg("successfully scraped %d items. FINISH" % self.items_scraped)
            reactor.stop()
