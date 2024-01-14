# import scrapy
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By

# class PSU_Spider(scrapy.Spider):
#     name = "psu"
    
#     def __init__(self):
#         self.chrome_options = webdriver.ChromeOptions()
#         self.service = Service(executable_path="C:\\Workspaces\\crawler-demo-f1\\crawler\\chromedriver.exe")
#         self.driver = webdriver.Chrome(service=self.service, options=self.chrome_options)

#     def start_requests(self):
#         urls = [
#             'https://pcpartpicker.com/products/power-supply/'
#             # 'https://books.toscrape.com/'
#         ]
#         for url in urls:
#             yield scrapy.Request(url=url, callback=self.parse)

#     def parse(self, response):
#          self.driver.get(response.url)
#          self.driver.maximize_window()
#          print(self.driver.find_element(By.TAG_NAME, "table").text)
#         # print(response.css('table').get())
#         #   Don't forget to quit the driver when you're done with it
#          self.driver.quit()

# No Selenium ------------------------------

import scrapy
import random
import time


class CPU_Spider(scrapy.Spider):
    name = "cpu"
    def start_requests(self):
        urls = [
             'https://pc-builder.net/cpu/'
            # 'https://www.getastra.com/'
            # 'https://books.toscrape.com/'
        ]
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
            'core_count': response.xpath("//tr/td/div[text()='Core Count']/following-sibling::div/text()").get(),
            'core_clock': response.xpath("//tr/td/div[text()='Performance Core Clock']/following-sibling::div/text()").get(),
            'boost_clock': response.xpath("//tr/td/div[text()='Performance Boost Clock']/following-sibling::div/text()").get(),
            'tdp':  response.xpath("//tr/td/div[text()='TDP']/following-sibling::div/text()").get(),
            'series':  response.xpath("//tr/td/div[text()='Series']/following-sibling::div/text()").get(),
            'microarchitecture':  response.xpath("//tr/td/div[text()='Microarchitecture']/following-sibling::div/text()").get(),
            'core_family':  response.xpath("//tr/td/div[text()='Core Family']/following-sibling::div/text()").get(),
            'socket':response.xpath("//tr/td/div[text()='Socket']/following-sibling::div/text()").get(),
            'integrated_graphics':response.xpath("//tr/td/div[text()='Integrated Graphics']/following-sibling::div/text()").get(),
            'max_memory_support': response.xpath("//tr/td/div[text()='Maximum Supported Memory']/following-sibling::div/text()").get(),
            'ecc_support': response.xpath("//tr/td/div[text()='ECC Support']/following-sibling::div/text()").get(),    
            'include_cooler':  response.xpath("//tr/td/div[text()='Include Cooler']/following-sibling::div/text()").get(), 
            'smt':response.xpath("//tr/td/div[text()='SMT']/following-sibling::div/text()").get(), 
            'packaging': response.xpath("//tr/td/div[text()='Packaging']/following-sibling::div/text()").get(),
            'l1_cache': response.xpath("//tr/td/div[text()='Performance L1 Cache']/following-sibling::div/text()").get(),
            'l2_cache':  response.xpath("//tr/td/div[text()='Performance L2 Cache']/following-sibling::div/text()").get(),
            'l3_cache':  response.xpath("//tr/td/div[text()='L3 Cache']/following-sibling::div/text()").get(),
            'lithography': response.xpath("//tr/td/div[text()='Lithography']/following-sibling::div/text()").get(),
            'cpu_cooler_included':response.xpath("//tr/td/div[text()='Includes CPU Cooler']/following-sibling::div/text()").get(),
            'multi_threading':response.xpath("//tr/td/div[text()='Simultaneous Multithreading']/following-sibling::div/text()").get()
        }

