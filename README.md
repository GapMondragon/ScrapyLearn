# ScrapyLearn
This tutorial is based on the video tutorial from John Watson Rooney at https://www.youtube.com/watch?v=s4jtkzHhLzY&ab_channel=JohnWatsonRooney

Before proceeding, make sure your system is up-to-date by running the following commands:
```
apt-get update
apt-get upgrade
```

Create a virtual environment and activate it by running the following commands:
```
python3 -m venv venv
source venv/bin/activate
```

Next, install the latest version of pip:
```
python -m pip install --upgrade pip
```

Install the scrapy library by running the following command:
```
pip3 install scrapy
```

Create a new Scrapy project by running the following command:
```
scrapy startproject primalBrew
```

Go to the primalBrew directory:
```
cd primalBrew
```

Access the Scrapy shell to check which parameters you need in your Spider file by running the following command:
```
scrapy shell
```

Fetch the web page of interest by running the following command and replacing [link] with the desired URL:
```
fetch('[link]')
```

In the example tutorial, we use the following website:  https://primalbrewcoffee.com/collections/single-origins
```
fetch('https://primalbrewcoffee.com/collections/single-origins')
```

Once you have fetched the web page, you can extract information from it as follows:
Get the first product that has the details:
```
products = response.css('div.grid-view-item')
```

Check the number of products:
```
len(products)
```

Get the title of the first product:
```
products.css('span.visually-hidden::text').get()
```

Get the titles of ALL products:
```
products.css('span.visually-hidden::text').getall()
```

Get the price of the first product:
```
products.css('span.price-item::text').get()
```
To remove the 'from $' and '\n' from the price, use the following code:
```
products.css('span.price-item::text').get()[6:-1]
```

Get the link/href of the first product:
```
products.css('a.grid-view-item__link').attrib['href']
```

To get the complete URL of the first product since it only return half of the URL, use the following code:
```
"https://primalbrewcoffee.com" + products.css('a.grid-view-item__link').attrib['href']
```

Get the next page button (if available on the website, only an example since primalBrew only has a single page for this product. This will be used to scrape):
```
response.css('a.action.next').attrib['href']
```

Now that we have tested how to get the data that we need:
Create a spider file in primalBrew/primalBrew/spiders/
for this one we will call it primalBrew_spider.py
edit it accordingly.

To run the spider and save the data to a file, use the following command, replacing primalB with the desired name for the spider and primal1.json with the desired name for the output file
```
scrapy crawl primalB -O primal1.json
```
