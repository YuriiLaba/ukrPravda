import scrapy

# and the result of the input processor is collected and kept inside the ItemLoader.
# After collecting all data, the ItemLoader.load_item() method is called to populate
# and get the populated Item object.
class Product(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    stock = scrapy.Field()
    title = scrapy.Field()
    last_updated = scrapy.Field(serializer=str)