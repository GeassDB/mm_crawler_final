import getopt, sys
from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy import log, signals
from spiders.mmspider import MmspiderSpider
from scrapy.utils.project import get_project_settings

class startSpider(object):
    def __init__(self):
        super(startSpider, self).__init__()
        self.number = 0
        self.location = ''
    def help_text(self):
        print """

    Usage: mm_crawler.py [-h Help] [-n Number] [-o Location] [-s Start]
        -h, --Help      Print help
        -n, --Number    Tread limit (default is 10)
        -o, --Location  pictures save location(default is ./pics)
        -s, --Start     start spider
        """

    def main(self):
        try:
            opts, args = getopt.getopt(
            	sys.argv[1:],
            	"hsn:f:",
            	["Help", "Start", "Number=", "Location="])
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
                    self.number = int(y)
                except ValueError as err:
                    print 'invalid input'
                    sys.exit()
            elif x in ("-o", "--Location"):
            	   self.location = y
            elif x in ("-s", "--Start"):
            	print 'spider running...'
                self.start()
            else:
                assert False, "unhandled option"

    def start(self):
        spider = MmspiderSpider()
        settings = get_project_settings()
        if self.location:
            settings.set('IMAGES_STORE', self.location)
        if self.number:
            settings.set('CONCURRENT_REQUESTS', self.number)
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
