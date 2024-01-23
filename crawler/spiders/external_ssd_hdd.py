import scrapy
import random
import time


class External_SSD_HDD_Spider(scrapy.Spider):
    name = "external_ssd_hdd"
    def start_requests(self):
        urls = ['https://pc-builder.net/external-ssd-hdd/page/']
        num_pages = 24
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
            'capacity': response.xpath("//tr/td/div[text()='Capacity']/following-sibling::div/text()").get(),
            'type': response.xpath("//tr/td/div[text()='Type']/following-sibling::div/text()").get(),
            'interface': response.xpath("//tr/td/div[text()='Interface']/following-sibling::div/text()").get(),
            'rpm': response.xpath("//tr/td/div[text()='RPM']/following-sibling::div/text()").get(),
            'price_per_gb': response.xpath("//tr/td/div[text()='Price / GB']/following-sibling::div/text()").get(),          
        }

