from scrapy import Spider
from scrapy.http import Request
from scrapy.selector import Selector
from newegg.items import scrapeGPU # Calls the class scrapeGPU() from item.py

class amazongpu(Spider):
    name = "amazongpu" # Name of the Spider
    allowed_domains = ["amazon.com"]
    rank = 1 # Ranking?

    def start_requests(self):
        start_urls = [
            "https://www.amazon.com/s?k=Computer+Graphics+Cards&i=computers&rh=n:284822&page=%&_encoding=UTF8&c=ts&qid=1608032958&ts_id=284822" # Start of the URL, % is the page number
            % page for page in list(range(1, 2))
        ]
        for url in start_urls:
            yield Request(url = url, callback = self.parse) # For each URL, go to parse function

    def parse(self, response):
        for index in range(len(31)): # For each product
            item = scrapeGPU() # Calls the class scrapeGPU() from item.py
            item['rank'] = self.rank # Working
            item['url'] = response.xpath('div[@class = "item-info"]/a/@href').get() # Working
            productname = response.xpath(f'//*[@id="search"]/div[1]/div[2]/div/span[3]/div[2]/div[{index}]/div/span/div/div/div[2]/div[2]/div/div[1]/div/div/div[1]/h2/a/span/text()').get() # Working
            if 'Refurbished' in productname or 'Open Box' in productname:
                continue
            item['productname'] = productname
            try:
                prevprice = product.xpath('div[@class = "item-info"]/div[@class = "item-action"]/ul/li[@class = "price-was"]/span/text()').get() # Not working
            except Exception as e:
                prevprice = None
            intprice = product.xpath("//div[@class='item-action']//strong//text()").get() # Get the Dollars, not working
            centprice = product.xpath("//div[@class='item-action']//sup//text()").get() # Get Cents, not working

            if not intprice: # If there's no price
                item['price'] = prevprice # Sub to previous price
            else:
                item['price'] = intprice + centprice # Else, add both of them together
            rating = product.xpath('//div[@class = "item-info"]/div[@class = "item-branding"]/a/@title').get() # Gets the rating
            if rating == []:
                item['rating'] = 'no rating'
            else:
                item['rating'] = rating # Working
            url = product.xpath('div[@class = "item-info"]/a/@href').get() # Gets the URL of the product
            request = Request(url, callback = self.productpage) # Forwards the URL to the productpage function
            request.meta['item'] = item
            self.rank += 1
            yield request # call the request

    def productpage(self, response):
        # Old Code
        # try:
        #     specs = response.xpath('/div[@class="tab-nav active"]')
        # except Exception as e:
        #     yield None
        # itemdict = {}
        # for i in specs:
        #     test = i.xpath('dl')
        #     for t in test:
        #         name = t.xpath('dt/text()').extract()
        #         if name == []:
        #             name = t.xpath('dt/a/text()').extract()
        #         itemdict[name[0]] = t.xpath('dd/text()').extract()[0]
        # item = response.meta['item']

        #item = scrapeGPU() # Calls the class scrapeGPU() from item.py
        #item['brand'] = response.xpath('//*[@id="product-details"]/div[2]/div[2]/table[1]/tbody/tr[1]/td')
        #item['model'] = response.xpath('//*[@id="product-details"]/div[2]/div[2]/table[1]/tbody/tr[3]/td')

        # Old Code
        # item['brand'] = itemdict.get('Brand', None)
        # item['model'] = itemdict.get('Model', None)
        # item['chipmake'] = itemdict.get('Chipset Manufacturer', None)
        # item['gpu'] = itemdict.get('GPU', None)
        # item['coreclock'] = itemdict.get('Core Clock', None)
        # item['boostclock'] = itemdict.get('Boost Clock', None)
        # item['memoryclock'] = itemdict.get('Effective Memory Clock', None)
        # item['memorysize'] = itemdict.get('Memory Size', None)
        # item['memoryinterface'] = itemdict.get('Memory Interface', None)
        # item['memorytype'] = itemdict.get('Memory Type', None)
        yield item
