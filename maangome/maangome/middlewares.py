import random
import json
import base64
import logging
from pymongo import MongoClient
from datetime import datetime

from scrapy.conf import settings
from scrapy.exceptions import IgnoreRequest

from maangome.settings import PROXIES_LIST, PROXY_SCHEME
from maangome.items import *

logger = logging.getLogger(__name__)
# client = MongoClient(MONGODB_SERVER)
# db = client[MONGODB_DB]


class RandomUserAgentMiddleware(object):
    def process_request(self, request, spider):
        ua = random.choice(settings.get('USER_AGENT_LIST'))
        if ua:
            request.headers['User-Agent'] = ua
        logger.debug("*** USER AGENT IS: " + request.headers['User-Agent'])


class HeadersMiddleware(object):
    def process_request(self, request, spider):
        request.headers['accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
        request.headers['accept-encoding'] = 'gzip, deflate, sdch'
        request.headers['accept-language'] = 'en-US,en;q=0.8'
        request.headers['upgrade-insecure-requests'] = '1'
        if 'Referer' in request.headers.keys():
            del request.headers['Referer']
        logger.debug("*** HEADERS ARE: " + json.dumps(request.headers))


class ProxyMiddleware(object):
    def process_request(self, request, spider):
        logger.debug("*** Proxy request Start")
        proxy = random.choice(PROXIES_LIST)
        request.meta['proxy'] = PROXY_SCHEME + proxy['ip_port']
        proxy_user_pass = proxy['user_pass']
        encoded_user_pass = base64.encodestring(proxy_user_pass)
        request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
        logger.debug("*** Proxy IP : %s" % (request.meta['proxy']))
        logger.debug("*** Proxy Auth : %s" % (request.headers['Proxy-Authorization']))
