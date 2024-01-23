import scrapy
import random
import time


class Cpu_Cooler_Spider(scrapy.Spider):
    name = "cpu_cooler"
    def start_requests(self):
        urls = ['https://pc-builder.net/cpu-cooler/page/']
        
        num_pages = 101
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
        model = response.xpath("//tr/td/div[text()='Model']/following-sibling::div/text()").get() \
                or response.css('h1::text').get()
        
        yield {
            'name': response.css('h1::text').get(),
            'img': response.css('main div div div img::attr(src)').get(),
            'price': response.css('div.text-4xl::text').get(),
            'part': response.xpath("//tr/td/div[text()='Part #']/following-sibling::div/text()").get(),
            
            'model': model,
            'manufacturer':response.xpath("//tr/td/div[text()='Manufacturer']/following-sibling::div/text()").get(),
            'color': response.xpath("//tr/td/div[text()='Color']/following-sibling::div/text()").get(),
            'water_cooled': response.xpath("//tr/td/div[text()='Water Cooled']/following-sibling::div/text()").get(),
            'radiator_size': response.xpath("//tr/td/div[text()='Radiator Size']/following-sibling::div/text()").get(),
            'fan_rpm': response.xpath("//tr/td/div[text()='Fan RPM']/following-sibling::div/text()").get(),
            'noise_level': response.xpath("//tr/td/div[text()='Noise Level']/following-sibling::div/text()").get(),
            'fanless': response.xpath("//tr/td/div[text()='Fanless']/following-sibling::div/text()").get(),
            'height': response.xpath("//tr/td/div[text()='Height']/following-sibling::div/text()").get(),
            'cpu_socket_compatibility': response.xpath("//tr/td/div[text()='CPU Socket']/following-sibling::div/text()").get(),
        }

