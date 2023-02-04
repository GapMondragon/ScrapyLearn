import scrapy

class PrimalBrewSpider(scrapy.Spider):
    name = 'primalB'
    start_urls = ['https://primalbrewcoffee.com/collections/single-origins']
    
    def parse(self, response):
        for products in response.css('div.grid-view-item'):
            try:
                # instead of return scrapy uses yield
                yield {
                    'name': products.css('span.visually-hidden::text').get(),
                    'price': products.css('span.price-item::text').get()[6:-1],
                    'link': "https://primalbrewcoffee.com" + products.css('a.grid-view-item__link').attrib['href']
                }
            except:
                yield {
                    'name': products.css('span.visually-hidden::text').get(),
                    'price': 'Sold out',
                    'link': "https://primalbrewcoffee.com" + products.css('a.grid-view-item__link').attrib['href']
                }

        next_page = response.css('a.action.next').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
            # if there is a next page button, 
            #   click next page then run parse function.