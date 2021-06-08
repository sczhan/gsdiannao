# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class E4XhwItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class XiaohuaItem(scrapy.Item):
    title = scrapy.Field()
    href = scrapy.Field()
    src = scrapy.Field()
    image_url = scrapy.Field()
    name = scrapy.Field()
