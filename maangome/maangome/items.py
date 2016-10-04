# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MaangomeItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    album = scrapy.Field()
    tracks = scrapy.Field()
    details = scrapy.Field()
    link = scrapy.Field()
