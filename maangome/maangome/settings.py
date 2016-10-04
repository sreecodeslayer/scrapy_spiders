# -*- coding: utf-8 -*-

# Scrapy settings for maangome project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'maangome'

SPIDER_MODULES = ['maangome.spiders']
NEWSPIDER_MODULE = 'maangome.spiders'
# *** USER USER_AGENT_LIST
DOWNLOADER_MIDDLEWARES = {
    'maangome.middlewares.RandomUserAgentMiddleware': 100,
    'maangome.middlewares.HeadersMiddleware': 101,
    'maangome.middlewares.ProxyMiddleware': 102,
}
USER_AGENT_LIST = ['Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.85 Safari/537.36',
                   'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)',
                    'Mozilla/5.0 (Windows; U; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)',
                    'Mozilla/5.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)',
                    'Mozilla/5.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4325)',
                    'Mozilla/5.0 (compatible; MSIE 6.0; Windows NT 5.1)',
                    'Mozilla/45.0 (compatible; MSIE 6.0; Windows NT 5.1)',
                    'Mozilla/4.08 (compatible; MSIE 6.0; Windows NT 5.1)',
                    'Mozilla/4.01 (compatible; MSIE 6.0; Windows NT 5.1)',
                    'Mozilla/4.0 (X11; MSIE 6.0; i686; .NET CLR 1.1.4322; .NET CLR 2.0.50727; FDM)',
                    'Mozilla/4.0 (Windows; MSIE 6.0; Windows NT 6.0)',
                    'Mozilla/4.0 (Windows; MSIE 6.0; Windows NT 5.2)',
                    'Mozilla/4.0 (Windows; MSIE 6.0; Windows NT 5.0)',
                    'Mozilla/4.0 (Windows; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727)',
                    'Mozilla/4.0 (MSIE 6.0; Windows NT 5.1)',
                    'Mozilla/4.0 (MSIE 6.0; Windows NT 5.0)',
                    'Mozilla/4.0 (compatible;MSIE 6.0;Windows 98;Q312461)',
                    'Mozilla/4.0 (Compatible; Windows NT 5.1; MSIE 6.0) (compatible; MSIE 6.0; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
                    'Mozilla/4.0 (compatible; U; MSIE 6.0; Windows NT 5.1) (Compatible; ; ; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)',
                    'Mozilla/4.0 (compatible; U; MSIE 6.0; Windows NT 5.1)',
                    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3; Tablet PC 2.0)',
                    'Opera/9.24 (X11; Linux i686; U; nl) | opera 9.24 on ubuntu 7.10 in dutch',
                    'Mozilla/5.0 (X11; Linux i686; U; nl; rv:1.8.0) Gecko/20060728 Firefox/1.5.0 Opera 9.24 | same, bu "identify as FF"',
                    'Mozilla/4.0 (compatible; MSIE 6.0; X11; Linux i686; nl) Opera 9.24 | same, but "identify as IE"',
                    'Mozilla/5.0 (X11; Linux i686; U; nl; rv:1.8.0) Gecko/20060728 Firefox/1.5.0 | same, but "MASK as FF"',
                    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; nl) | same, but "MASK as IE"',
                    'Mozilla/5.0 (compatible; U; ABrowse 0.6; Syllable) AppleWebKit/420+ (KHTML, like Gecko)',
                    'Mozilla/5.0 (BeOS; U; Haiku BePC; en-US; rv:1.8.1.21pre) Gecko/20090227 BonEcho/2.0.0.21pre',
                    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1.9) Gecko/20071113 BonEcho/2.0.0.9',
                    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1) Gecko/20061026 BonEcho/2.0',
                    'Mozilla/5.0 (X11; 78; CentOS; US-en) AppleWebKit/527+ (KHTML, like Gecko) Bolt/0.862 Version/3.0 Safari/523.15',
                    'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; BOLT/2.514) AppleWebKit/534.6 (KHTML, like Gecko) Version/5.0 Safari/534.6.3',
                    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) RockMelt/0.8.36.78 Chrome/7.0.517.44 Safari/534.7',
                    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) RockMelt/0.8.34.841 Chrome/6.0.472.63 Safari/534.3',
                    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.7 (KHTML, like Gecko) RockMelt/0.8.36.74 Chrome/7.0.517.44 Safari/534.7',
                    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) RockMelt/0.8.40.147 Chrome/8.0.552.231 Safari/534.10',
                    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-US) AppleWebKit/534.10 (KHTML, like Gecko) RockMelt/0.8.40.147 Chrome/8.0.552.231 Safari/534.10',
                    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.10 (KHTML, like Gecko) RockMelt/0.8.40.147 Chrome/8.0.552.231 Safari/534.10',
                    'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-US) AppleWebKit/534.13 (KHTML, like Gecko) RockMelt/0.9.48.51 Chrome/9.0.597.107 Safari/534.13',
                    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) RockMelt/0.9.58.494 Chrome/11.0.696.71 Safari/534.24',
                    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_7) AppleWebKit/534.24 (KHTML, like Gecko) RockMelt/0.9.58.478 Chrome/11.0.696.71 Safari/534.24',]

# *** PROXIES
PROXY_SCHEME = 'http://'
PROXIES_LIST = [
    {'ip_port': '195.154.161.95:6891', 'user_pass': 'jimcarney:Qxiai6w'},
    {'ip_port': '195.154.161.95:6892', 'user_pass': 'jimcarney:Qxiai6w'},
    {'ip_port': '195.154.161.95:6893', 'user_pass': 'jimcarney:Qxiai6w'},
    {'ip_port': '195.154.161.95:6894', 'user_pass': 'jimcarney:Qxiai6w'},
    {'ip_port': '195.154.161.95:6895', 'user_pass': 'jimcarney:Qxiai6w'},
]


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'maangome (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'maangome.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'maangome.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'maangome.pipelines.SomePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
