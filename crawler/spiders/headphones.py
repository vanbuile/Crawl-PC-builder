import scrapy
import random
import time


class Headphones_Spider(scrapy.Spider):
    name = "headphones"
    page_number = 1
    def start_requests(self):
        urls = ['https://pc-builder.net/headphones/page/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
        num_pages = 137
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
            'type': response.xpath("//tr/td/div[text()='Type']/following-sibling::div/text()").get(),
            'frequency_response': response.xpath("//tr/td/div[text()='Frequency Response']/following-sibling::div/text()").get(),
            'impedance': response.xpath("//tr/td/div[text()='Impedance']/following-sibling::div/text()").get(),
            'sensitive_at_1V_rms': response.xpath("//tr/td/div[text()='Sensitivity at 1 V RMS']/following-sibling::div/text()").get(),
            'connection': response.xpath("//tr/td/div[text()='Connection']/following-sibling::div/text()").get(),
            'cord_length': response.xpath("//tr/td/div[text()='Cord Length']/following-sibling::div/text()").get(),
            'microphone': response.xpath("//tr/td/div[text()='Microphone']/following-sibling::div/text()").get(),
            'wireless': response.xpath("//tr/td/div[text()='Wireless']/following-sibling::div/text()").get(),
            'enclosure_type': response.xpath("//tr/td/div[text()='Enclosure Type']/following-sibling::div/text()").get(),
            'active_noise_cancelling': response.xpath("//tr/td/div[text()='Active Noise Cancelling']/following-sibling::div/text()").get(),
            'channels': response.xpath("//tr/td/div[text()='Channels']/following-sibling::div/text()").get(),
        }

