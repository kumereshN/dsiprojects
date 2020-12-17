# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class scrapeGPU(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    productname = Field()
    brand = Field()
    model = Field()
    chipmake = Field()
    gpu = Field()
    coreclock = Field()
    boostclock = Field()
    memoryclock = Field()
    memorysize = Field()
    memoryinterface = Field()
    memorytype = Field()
    price = Field()
    rating = Field()
    url = Field()
    rank = Field()
