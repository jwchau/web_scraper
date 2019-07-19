# -*- coding: utf-8 -*-
import scrapy


class AmazonSpider(scrapy.Spider):
    name = 'amazon'
    allowed_domains = ['amazon.com']
    start_urls = ['https://www.amazon.com/s?k=laptop&i=computers&rh=n%3A13896617011%2Cp_85%3A2470955011%2Cp_72%3A1248879011%2Cp_36%3A10000-25000%2Cp_n_size_browse-bin%3A2423840011%2Cp_n_feature_five_browse-bin%3A7817222011%2Cp_n_operating_system_browse-bin%3A17702486011&dc&crid=3G334NDQTHNUL&qid=1563568378&rnid=562215011&sprefix=laptop%2Caps%2C230&ref=sr_nr_p_n_operating_system_browse-bin_1']

    def parse(self, response):
        self.log('I just visited: ' + response.url)
        yield {
            'title': ,
            'price': ,
            'sold_by': ,
        }

#got the names
for title in response.css('span.a-size-medium::text').extract():
    print (title)
    print ('\n')



item = response.css('.a-link-normal .a-text-normal::attr(href)').extract()
price = response.css('.a-price-whole::text').extract()
































#end of file
