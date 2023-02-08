import scrapy

class PrimalBrewSpider(scrapy.Spider):
    # name to call the spider
    name = 'primalB'
    # url of the page
    start_urls = ['https://primalbrewcoffee.com/collections/single-origins']
    
    # parse function for ETL
    # self | refers to itself as a function within this class
    # response | is what we looked at our shell
    def parse(self, response):
        # identify each product within this div
        for products in response.css('div.grid-view-item'):
            try:
                # scrapy uses yield instead of return
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
        # for multiple pages / pagination
        
        # look for next page button 
        next_page = response.css('a.action.next').attrib['href']
        # if the next_page(the button) exists condition
        if next_page is not None:
            # click the button then run parse function.
            yield response.follow(next_page, callback=self.parse)
            