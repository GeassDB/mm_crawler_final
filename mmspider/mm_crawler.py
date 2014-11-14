from scrapy.utils.project import get_project_settings
settings = get_project_settings()
settings.setdict({
    'SPIDER_MODULES' : ['mmspider.spiders'],
    'NEWSPIDER_MODULE' : 'mmspider.spiders',
    'ITEM_PIPELINES' : {'scrapy.contrib.pipeline.images.ImagesPipeline': 1},
    'IMAGES_STORE' : './pics',
    'IMAGE_MIN_HEIGHT' : 120,
    'IMAGE_MIN_WIDTH' : 120,
    'DOWNLOAD_DELAY' : 2,
    'CONCURRENT_REQUESTS' : 10,
    'USER_AGENT' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36',
    'EXTENSIONS' : {'limitcount.LimitCountExtension':None}
})

import getopt, sys
from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy import log, signals
from spiders.mmspider import MmspiderSpider
from scrapy.utils.project import get_project_settings

class startSpider(object):
    def __init__(self):
        super(startSpider, self).__init__()
        self.numb = 10
        self.location = './pics'
        self.limit = 0
    def help_text(self):
        print """

    Usage: mm_crawler.py [-h Help] [-n Number] [-o Location] [-l Limit]
        -h, --Help      Print help
        -n, --Number    Tread limit            (default  10)
        -o, --Location  pictures save location (default ./pics)
        -l, --Limit     pic limit              (default 0)
        """


    def main(self):
        try:
            opts, args = getopt.getopt(
            	sys.argv[1:],
            	"hn:o:l:",
            	["Help", "Number=", "Location=","Limit="])
        except getopt.GetoptError as err:
            # print help information and exit:
            print str(err) # will print something like "option -a not recognized"
            sys.exit(2)
        for x, y in opts:
            if x in ("-h", "--Help"):
                self.help_text()
                sys.exit()
            elif x in ("-n", "--Number"):
                try:
                    self.numb = int(y)
                    settings.setdict({
                        'CONCURRENT_REQUESTS' : self.numb
                    })
                except ValueError as err:
                    print 'invalid input'
                    sys.exit()
            elif x in ("-o", "--Location"):
            	   self.location = y
                   settings.setdict({
                       'IMAGES_STORE' : self.location
                   })
            elif x in ("-l", "--Limit"):
                self.limit = y
                if self.limit.isdigit():
                    if self.limit>0:
                        settings.setdict({
                            'EXTENSIONS' : {'limitcount.LimitCountExtension':500},
                            'MAX_DOWNLOAD_COUNT' : self.limit
                        })
                else:
                    print 'ERROR: argument for -l should be a number'
                    sys.exit()
            else:
                assert False, "unhandled option"
        self.start()

    def start(self):
        spider = MmspiderSpider()
        if self.location:
            settings.set('IMAGES_STORE', self.location)
        if self.numb:
            settings.set('CONCURRENT_REQUESTS', self.numb)
        print settings.get('IMAGES_STORE'), settings.get('CONCURRENT_REQUESTS')

        crawler = Crawler(settings)
        crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
        crawler.configure()
        crawler.crawl(spider)
        crawler.start()
        log.start()
        reactor.run()

if __name__ == "__main__":
    startSpider().main()
