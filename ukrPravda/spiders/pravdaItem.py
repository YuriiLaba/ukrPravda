# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader
from pravdaItemHelper import Product
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http import Request
from scrapy.spider import BaseSpider

from scrapy.loader.processors import TakeFirst, MapCompose, Join
from w3lib.html import remove_tags
import ukrPravda.items

# The input processor processes the extracted data as soon as it’s received
# and the result of the input processor is collected and kept inside the ItemLoader.
# After collecting all data, the ItemLoader.load_item() method is called to populate
# and get the populated Item object.


class PravdaitemSpider(scrapy.Spider):
    name = "pravdaItem"
    allowed_domains = ["pravda.com.ua"]

    start_urls = [
        'http://blogs.pravda.com.ua',
    ]
        #'http: // brovary.pravo - znaty.org.ua / tag / novini /',

    def parse(self, response):
        #l = ItemLoader(item=Product(), response=response)
        # Data from xpath1 is extracted, and passed through the input processor of the name field. The result of the
        # input processor is collected and kept in the Item Loader (but not yet assigned to the item).
        #l.add_css("title", "h1.post-title::text")


        #for i in response.css('title::text').extract():
            #l.add_css("title", i.encode(utf-8))
        #l.add_xpath('name', '//div[@class="product_title"]')
        #l.add_css("title", 'title::text')

        #l.add_css("img", "a > .wp-post-image::attr(src)")
        #l.add_css("tags", ".bs-cat a::text, .bs-tags a::text")

        #l.add_css("text", ".pf-content")
        #l.add_css("date_of_publish", '.rp-date')
        #l.add_css("source", '.ai-info h6 a::text')
        #l.add_value("url", response.url)
        #yield l.load_item()



            l = ItemLoader(item=Product(), response=response)
            l.add_css("author", '.bauthor::text')
            l.add_css("title", ".btitle::text")
            l.add_css("date_of_publish", '.bdate::text')
            yield l.load_item()

            with open('blog_data.txt', 'a') as f:
                title_list = l.get_output_value('title')
                author_list = l.get_output_value('author')
                data_list = l.get_output_value('date_of_publish')

                for author in author_list:
                    f.write('author: {0}\n'.format(author.encode('utf-8')))

                for title in title_list:

                    f.write('title: {0}\n'.format(title.encode('utf-8')))

                for data in data_list:

                    f.write('data: {0}\n'.format(data.encode('utf-8')))
