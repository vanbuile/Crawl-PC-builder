import scrapy
import random
import time
import json

class Number_Of_Pages_Spider(scrapy.Spider):
    name = "number_of_pages"
    def start_requests(self):
        url = 'https://pc-builder.net/'
        endpoints = ['cpu', 'ram', 'laptop', 'power-supply', 'case', 'case-fan', 'fan-controller', 
                     'motherboard', 'optical drive', 'sound_card', 'ups', 'cpu-cooler', 'internal-ssd-hdd', 
                     'external-ssd-hdd', 'graphics-card', 'monitor', 'keyboard', 'mouse', 'thermal-paste',  
                     'headphones', 'speakers', 'wired-network-card', 'wifi-card']
        for endpoint in endpoints:
            target_url = url + endpoint
            sleep_time = random.uniform(1, 3)
            time.sleep(sleep_time)
            num_pages = scrapy.Request(url=target_url, callback=self.parse)
            print("numpages: ",num_pages)
            with open('number-of-pages.json', 'w') as file:
                json.dump({endpoint: num_pages}, file)

    def parse(self, response):
        num_pages = response.css('nav > a:nth-last-child(2)::text').get()
        yield int(num_pages)

        

