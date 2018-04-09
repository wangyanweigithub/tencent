# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TecentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class CityLink(scrapy.Item):
    city = scrapy.Field()
    link = scrapy.Field()


class AreaCode(scrapy.Item):
    city = scrapy.Field()
    area_name = scrapy.Field()
    area_code = scrapy.Field()