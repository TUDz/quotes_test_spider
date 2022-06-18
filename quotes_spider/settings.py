### This is only used for testing purposes on dev environment
import os
ZYTE_SMARTPROXY_APIKEY = os.getenv('ZYTE_KEY')
BOT_NAME = 'quotes_spider'

SPIDER_MODULES = ['quotes_spider.spiders']
NEWSPIDER_MODULE = 'quotes_spider.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1"

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

DOWNLOADER_MIDDLEWARES = {
    "scrapy_zyte_smartproxy.ZyteSmartProxyMiddleware": 610
    }
ZYTE_SMARTPROXY_ENABLED = True
CONCURRENT_REQUESTS_PER_DOMAIN = 8
DOWNLOAD_DELAY = 5
AUTOTHROTTLE_ENABLED = True
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
    "quotes_spider.pipelines.QuotesSpiderPipeline": 300
}