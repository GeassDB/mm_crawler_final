mm_crawler_final
================


/n Usage: mm_crawler.py [-h Help] [-n Number] [-o Location] [-s Start]
/n        -h, --Help      Print help
/n        -n, --Number    Tread limit (default is 10)
/n        -o, --Location  pictures save location(default is ./pics)
/n        -s, --Start     start spider
/n
/n 实现了多线程爬虫 
/n 可以用-n 参数指定线程数    默认10
/n 通过DOWNLOAD_DELAY = 2 延时下载防止被狗
/n middlewares.py 和settings里的注释
"#DOWNLOADER_MIDDLEWARES = {
#    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
#    'pythontab.middlewares.ProxyMiddleware': 100,"
/n 可以通过代理来饶过安全狗
/n 图片保存在pics目录下   可以通过-o参数修改
