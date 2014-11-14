mm_crawler_final
================


 Usage: mm_crawler.py [-h Help] [-n Number] [-o Location] [-l Limit]
        -h, --Help      Print help
        -n, --Number    Tread limit (default  10)
        -o, --Location  pictures save location(default ./pics)
        -l, --Limit     pic limit    (default 0)
        
        
 实现了多线程爬虫 
 ---------------------------------------------
 可以用-n 参数指定线程数    默认10

 -----------------------------------------------
 通过DOWNLOAD_DELAY = 2 延时下载防止被狗
 -----------------------------------------------
 middlewares.py 和settings里的注释:
 
"#DOWNLOADER_MIDDLEWARES = {
#    'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
#    'pythontab.middlewares.ProxyMiddleware': 100,"
 ----------------------------------------------
 可以通过代理来饶过安全狗
 -----------------------------------------------
 图片默认保存在pics目录下   可以通过-o参数修改
 -----------------------
 -l 参数 指定下载图片数量限制
