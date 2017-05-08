# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class YtsItem(scrapy.Item):
	# define the fields for your item here like:
	# name = scrapy.Field()
	name = scrapy.Field()
	year = scrapy.Field()
	genre = scrapy.Field()
	imdb_rating = scrapy.Field()
	url = scrapy.Field()
	magnet_1080 = scrapy.Field()
