import scrapy

#my_url = https://www.amazon.com/s?k=laptop&i=computers&rh=n%3A13896617011%2Cp_85%3A2470955011%2Cp_72%3A1248879011%2Cp_36%3A10000-25000%2Cp_n_size_browse-bin%3A2423840011%2Cp_n_feature_five_browse-bin%3A7817222011%2Cp_n_operating_system_browse-bin%3A17702486011&dc&crid=3G334NDQTHNUL&qid=1563568378&rnid=562215011&sprefix=laptop%2Caps%2C230&ref=sr_nr_p_n_operating_system_browse-bin_1
class amazonSpider(scrapy.Spider):
    name = "products"

    def start_requests(self):
        urls = [
            'https://www.amazon.com/s?k=laptop&i=computers&rh=n%3A13896617011%2Cp_85%3A2470955011%2Cp_72%3A1248879011%2Cp_36%3A10000-25000%2Cp_n_size_browse-bin%3A2423840011%2Cp_n_feature_five_browse-bin%3A7817222011%2Cp_n_operating_system_browse-bin%3A17702486011&dc&crid=3G334NDQTHNUL&qid=1563568378&rnid=562215011&sprefix=laptop%2Caps%2C230&ref=sr_nr_p_n_operating_system_browse-bin_1'

        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        #page = response.url.split("/")[-2]
        #filename = 'quotes-%s.html' % page
        filename = 'results.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file: results')
