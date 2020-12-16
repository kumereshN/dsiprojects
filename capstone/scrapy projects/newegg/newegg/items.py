# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

from scrapy import Item, Field

class scrapeGPU(Item):
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
