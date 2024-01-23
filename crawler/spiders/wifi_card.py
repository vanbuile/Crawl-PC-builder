import scrapy
import random
import time


class Wifi_Card_Spider(scrapy.Spider):
    name = "wifi_card"
    page_number = 1
    def start_requests(self):
        urls = ['https://pc-builder.net/wifi-card/page/']
        # for url in start_urls:
        #     yield scrapy.Request(url=url, callback=self.parse)
        num_pages = 17
        for i in range(1, num_pages+1):
            sleep_time = random.uniform(1, 3)
            time.sleep(sleep_time)
            yield scrapy.Request(url=urls[0] + str(i), callback=self.parse)
        
    def parse(self, response):
        for item in response.css('table > tbody > tr'):
            item_link ='https://pc-builder.net'+ item.css('td:nth-child(1) a::attr(href)').get()
            if item_link is not None:
                sleep_time = random.uniform(1, 3)
                time.sleep(sleep_time)
                yield response.follow(item_link, callback=self.parse_item)

    def parse_item(self, response):
        
        yield {
            'name': response.css('h1::text').get(),
            'img': response.css('main div div div img::attr(src)').get(),
            'price': response.css('div.text-4xl::text').get(),
            'manufacturer':response.xpath("//tr/td/div[text()='Manufacturer']/following-sibling::div/text()").get(),
            'part': response.xpath("//tr/td/div[text()='Part #']/following-sibling::div/text()").get(),
            
            'color': response.xpath("//tr/td/div[text()='Color']/following-sibling::div/text()").get(),
            'interface': response.xpath("//tr/td/div[text()='Interface']/following-sibling::div/text()").get(),
            'protocol': response.xpath("//tr/td/div[text()='Protocol']/following-sibling::div/text()").get(),
            'antenna': response.xpath("//tr/td/div[text()='Antenna']/following-sibling::div/text()").get(),
        }

