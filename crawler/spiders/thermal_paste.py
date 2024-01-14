import scrapy
import random
import time


class Thermal_Paste_Spider(scrapy.Spider):
    name = "thermal_paste"
    def start_requests(self):
        urls = ['https://pc-builder.net/thermal-paste/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
        # for i in range(2, 11):
        #     sleep_time = random.uniform(1, 3)
        #     time.sleep(sleep_time)
        #     yield scrapy.Request(url=f'https://pc-builder.net/cpu/page/{i}', callback=self.parse)
        
            
    def parse(self, response):
        for item in response.css('table > tbody > tr'):
            item_link ='https://pc-builder.net'+ item.css('td:nth-child(1) a::attr(href)').get()
            if item_link is not None:
                sleep_time = random.uniform(1, 3)
                time.sleep(sleep_time)
                yield response.follow(item_link, callback=self.parse_item)
            # yield {
            #     'name': item.css('td:nth-child(2) a::text').get(),
            #     'link': item.css('td:nth-child(1) a::attr(href)').get()
            # }
        # Access next page
        # next_page = response.css('a.next-page-link::attr(href)').get()
        # if next_page is not None:
        #     sleep_time = random.uniform(1, 3)
        #     time.sleep(sleep_time)
        #     yield response.follow(next_page, callback=self.parse)
    def parse_item(self, response):
        yield {
            'name': response.css('h1::text').get(),
            'img': response.css('main div div div img::attr(src)').get(),
            'price': response.css('div.text-4xl::text').get(),
            'manufacturer':response.xpath("//tr/td/div[text()='Manufacturer']/following-sibling::div/text()").get(),
            'part': response.xpath("//tr/td/div[text()='Part #']/following-sibling::div/text()").get(),
            'amount': response.xpath("//tr/td/div[text()='Amount']/following-sibling::div/text()").get()
        }

