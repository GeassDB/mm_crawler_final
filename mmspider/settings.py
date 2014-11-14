# -*- coding: utf-8 -*-

# Scrapy settings for mmspider project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'mmspider'

SPIDER_MODULES = ['mmspider.spiders']
NEWSPIDER_MODULE = 'mmspider.spiders'
ITEM_PIPELINES = {'scrapy.contrib.pipeline.images.ImagesPipeline': 1}
IMAGES_STORE = '../pictures'
IMAGE_MIN_HEIGHT = 120
IMAGE_MIN_WIDTH = 120
DOWNLOAD_DELAY = 2
CONCURRENT_REQUESTS = 10
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'mmspider (+http://www.yourdomain.com)'
