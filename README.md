# ScrapyLearn
Tutorial from https://www.youtube.com/watch?v=s4jtkzHhLzY&ab_channel=JohnWatsonRooney

make sure to:
'apt-get update'
'apt-get upgrade'


python3 -m venv venv

<!-- go in venv -->
source venv/bin/activate

install latest pip version
    python -m pip install --upgrade pip

pip3 install scrapy

scrapy startproject primalBrew

<!-- go to dir -->
cd primalBrew

-----------

<!-- access shell -->
scrapy shell
<!-- add link -->
    fetch('https://primalbrewcoffee.com/collections/single-origins')
<!-- the first product that has the details -->
    products = response.css('div.grid-view-item')

<!-- check the number of products -->
    len(products)
        5
<!-- get title -->
    products.css('span.visually-hidden::text').get()
        'Brazil Santos | Single Origin'
<!-- get ALL titles -->
    products.css('span.visually-hidden::text').getall()
<!-- get price -->
    products.css('span.price-item::text').get()
        'from $50.00\n'
    products.css('span.price-item::text').get()[6:-1]
        '50.00'
<!-- get href -->
    products.css('a.grid-view-item__link').attrib['href']
        '/collections/single-origins/products/brazil-santos'
    "https://primalbrewcoffee.com" + products.css('a.grid-view-item__link').attrib['href']

<!-- go to next page (not here in this site) -->
    response.css('a.action.next').attrib['href']



<!-- running and saving file -->
<!-- primalB is the name given to the spider -->

<!-- test if it works. make a json or csv file -->
<!-- upper case -O will OVERWRITE
    lower case -o will append it
-->

    scrapy crawl primalB -O primal1.json




<!-- if you have multiple words with spaces in a class, 
    just put a period '.'   e.g
        'a.action  next'
        should be 'a.action.next'
 -->