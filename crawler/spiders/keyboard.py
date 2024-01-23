import scrapy
import random
import time


class Keyboard_Spider(scrapy.Spider):
    name = "keyboard"
    page_number = 1
    def start_requests(self):
        urls = ['https://pc-builder.net/keyboard/page/']
        
        num_pages = 140
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
            
            'style': response.xpath("//tr/td/div[text()='Style']/following-sibling::div/text()").get(),
            'color': response.xpath("//tr/td/div[text()='Color']/following-sibling::div/text()").get(),
            'mechanical': response.xpath("//tr/td/div[text()='Mechanical']/following-sibling::div/text()").get(),
            'switch_type': response.xpath("//tr/td/div[text()='Switch Type']/following-sibling::div/text()").get(),
            'backlit': response.xpath("//tr/td/div[text()='Backlit']/following-sibling::div/text()").get(),
            'mechanical': response.xpath("//tr/td/div[text()='Mechanical']/following-sibling::div/text()").get(),
            'connection_type': response.xpath("//tr/td/div[text()='Connection Type']/following-sibling::div/text()").get(),
            'tenkeyless': response.xpath("//tr/td/div[text()='Tenkeyless']/following-sibling::div/text()").get(),
            'normal_keys': response.xpath("//tr/td/div[text()='Normal Keys']/following-sibling::div/text()").get(),
            'mouse_included': response.xpath("//tr/td/div[text()='Mouse Included']/following-sibling::div/text()").get(),
            'mouse_color': response.xpath("//tr/td/div[text()='Mouse Color']/following-sibling::div/text()").get(),
            'mouse_hand_orientation': response.xpath("//tr/td/div[text()='Mouse Hand Orientation']/following-sibling::div/text()").get(),
        }

