import scrapy
# and the result of the input processor is collected and kept inside the ItemLoader.
# After collecting all data, the ItemLoader.load_item() method is called to populate
# and get the populated Item object.
from scrapy.loader.processors import TakeFirst


class Product(scrapy.Item):
    output_processor = TakeFirst()
    author = scrapy.Field()

    title = scrapy.Field()
    date_of_publish = scrapy.Field()