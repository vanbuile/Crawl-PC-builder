# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
class PsuItem(scrapy.Item):
    # define the fields for your PSU item here like:
    name = scrapy.Field()
    price = scrapy.Field()
    discount = scrapy.Field()
    brand = scrapy.Field()
    type = scrapy.Field()
    input_voltage = scrapy.Field()
    wattage = scrapy.Field()
    fan = scrapy.Field()
    size_1 = scrapy.Field()
    size_2 = scrapy.Field()
    size_3 = scrapy.Field()
    material = scrapy.Field()
    pass
