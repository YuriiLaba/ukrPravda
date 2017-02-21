import scrapy
#for i in (response.css("div.article__title a::text").extract()): print(i.encode('utf-8'))
#for i in response.css('title::text').extract(): print (i.encode('utf -8'))

class PravdaSpider(scrapy.Spider):
    name = "pravdaSpider"

    def start_requests(self):
        urls = [
            'http://www.pravda.com.ua/news/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        file_name = open('Main News.html','w')
        main_news = response.css(".news.news_all .article.article_bold")

        for i in (main_news.css(" .article__title a::text").extract()):
            file_name.write(i.encode('utf-8'))
            file_name.write('\n')

        file_name.close()
 


