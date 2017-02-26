# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from pravdaItemHelper import Product
from scrapy.loader.processors import TakeFirst, MapCompose, Join
from w3lib.html import remove_tags
import ukrPravda.items

# The input processor processes the extracted data as soon as it’s received
# and the result of the input processor is collected and kept inside the ItemLoader.
# After collecting all data, the ItemLoader.load_item() method is called to populate
# and get the populated Item object.


class PravdaitemSpider(scrapy.Spider):
    name = "pravdaItem"
    allowed_domains = ["pravdaItem"]
    start_urls = (
        'http://www.pravda.com.ua',
        #'http: // brovary.pravo - znaty.org.ua / tag / novini /',
    )

    def parse(self, response):
        l = ItemLoader(item=Product(), response=response)
        # Data from xpath1 is extracted, and passed through the input processor of the name field. The result of the
        # input processor is collected and kept in the Item Loader (but not yet assigned to the item).
        #l.add_css("title", "h1.post-title::text")


        #for i in response.css('title::text').extract():
            #l.add_css("title", i.encode(utf-8))

        l.add_css("title", 'title::text')

        #l.add_css("img", "a > .wp-post-image::attr(src)")
        #l.add_css("tags", ".bs-cat a::text, .bs-tags a::text")

        #l.add_css("text", ".pf-content")
        #l.add_css("date_of_publish", '.rp-date')
        #l.add_css("source", '.ai-info h6 a::text')
        #l.add_value("url", response.url)
        yield l.load_item()