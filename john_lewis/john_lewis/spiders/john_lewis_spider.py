# -*- coding: utf-8 -*-
import scrapy
from john_lewis.items import JohnLewisItem

class JohnLewisSpiderSpider(scrapy.Spider):
	name = "john_lewis_spider"
	allowed_domains = ["johnlewis.com"]
	start_urls = ['https://www.johnlewis.com/brands']

	def parse(self, response):
		BRANDS = "//li[@class='brand-entry']//a//@href"
		brands = response.xpath(BRANDS).extract()
		brands_ = ['https://www.johnlewis.com'+i for i in brands]
		for url in brands_:
			yield scrapy.Request(url = url, callback = self.parse_brands)

	def parse_brands(self, response):
		ITEM_LINK = "//div[@class='qv-image-holder']//a[@class='product-link']//@href"
		item_links = response.xpath(ITEM_LINK).extract()
		item_links_ = ['https://www.johnlewis.com'+i for i in item_links]
		for url in item_links_:
			yield scrapy.Request(url=url, callback=self.parse_item)

		NEXT = "//li[@class='next']//@href"
		try:
			next_page = response.xpath(NEXT).extract()[0]
			yield scrapy.Request(url=next_page, callback=self.parse_brands)
		except:
			pass

	def parse_item(self, response):
		NAME = "//span[@itemprop='name']//text()"
		name = response.xpath(NAME).extract_first().strip()

		PRICE = "//span[@itemprop='price']//text()"
		price = response.xpath(PRICE).extract_first().strip()

		CODE = "//div[@id='prod-product-code']//p//text()"
		code = response.xpath(CODE).extract_first().strip()

		IMAGE = "//img[@itemprop='image']//@src"
		image_url = response.xpath(IMAGE).extract_first().strip().replace('//','http://')

		url = response.url

		yield JohnLewisItem(url=url,name=name,price=price,code=code,image_url=image_url)