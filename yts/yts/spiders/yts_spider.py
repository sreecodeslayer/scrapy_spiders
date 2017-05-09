# -*- coding: utf-8 -*-
import scrapy
from yts.items import YtsItem

from pymongo import MongoClient

coll = MongoClient('mongodb://rootuser:passme123@localhost:27045')['yts']['all']
coll.drop()

class YtsSpiderSpider(scrapy.Spider):
	name = "yts_spider"
	allowed_domains = ["yts.ag"]
	start_urls = ['https://yts.ag/browse-movies/']

	def parse(self, response):
		LINK = "//section//a[@class='browse-movie-title']//@href"
		links = response.xpath(LINK).extract()
		for link in links:
			print link
			yield scrapy.Request(url=link, callback=self.parse_movie)

		NEXT = "//a[contains(text(),'Next')]//@href"
		next_page = response.xpath(NEXT).extract_first()
		next_page = 'https://yts.ag'+next_page if next_page else None
		if next_page is not None:
			print "NEXT PAGE >>>>>>>>>>>>>", next_page
			yield scrapy.Request(url=next_page, callback=self.parse)

	def parse_movie(self, response):

		print ".............."
		NAME = "//div[@id='movie-info']//h1//text()"
		YEAR = "//div[@id='movie-info']//h2//text()"
		GENRE = "//div[@id='movie-info']//h2//text()"
		IMDB_RATING = "//div[@class='bottom-info']//span[@itemprop='ratingValue']//text()"
		MAGNET = "//a[@class='magnet-download download-torrent magnet' and contains(@title,'1080p')]//@href"
		try:
			name = response.xpath(NAME).extract_first().strip()
			print name
		except:
			name = ''

		try:
			year = response.xpath(YEAR).extract_first().strip()
		except:
			year = ''

		try:
			genre = response.xpath(GENRE).extract()[-1].strip()
			genre = genre.replace('/',',')
		except:
			genre = ''

		try:
			imdb_rating = response.xpath(IMDB_RATING).extract_first().strip()
		except:
			imdb_rating = ''

		try:
			url = response.url
		except:
			url = ''

		try:
			mag_1080 = response.xpath(MAGNET).extract_first()
		except:
			mag_1080 = ''

		coll.insert({'name':name,
				'year':year,
				'genre':genre,
				'imdb_rating':imdb_rating,
				'url':url,
				'magnet-1080':mag_1080})
		yield YtsItem(
				name=name,
				year=year,
				genre=genre,
				imdb_rating=imdb_rating,
				url=url,
				magnet_1080=mag_1080)
