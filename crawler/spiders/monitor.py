import scrapy
import random
import time


class Monitor_Spider(scrapy.Spider):
    name = "monitor"
    def start_requests(self):
        urls = ['https://pc-builder.net/monitor/page/']
        
        num_pages = 209
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
        adaptive_sync = response.xpath("//tr/td/div[text()='Adaptive Sync']/following-sibling::div/text()").get() \
                        or response.xpath("//tr/td/div[text()='Frame Sync']/following-sibling::div/text()").get() \
                        or "None"
        response_time = response.xpath("//tr/td/div[text()='Response Time']/following-sibling::div/text()").get() \
                        or response.xpath("//tr/td/div[text()='Response Time (G2G)']/following-sibling::div/text()").get() \
                        or response.xpath("//tr/td/div[text()='Response Time (MPRT)']/following-sibling::div/text()").get() \
                        or "None"
        model = response.xpath("//tr/td/div[text()='Model']/following-sibling::div/text()").get() \
                        or response.css('h1::text').get()
                
        yield {
            'name': response.css('h1::text').get(),
            'img': response.css('main div div div img::attr(src)').get(),
            'price': response.css('div.text-4xl::text').get(),
            'part': response.xpath("//tr/td/div[text()='Part #']/following-sibling::div/text()").get(),
            
            'manufacturer':response.xpath("//tr/td/div[text()='Manufacturer']/following-sibling::div/text()").get(),
            'model': model,
            'resolution': response.xpath("//tr/td/div[text()='Resolution']/following-sibling::div/text()").get(),
            'screen_size': response.xpath("//tr/td/div[text()='Screen Size']/following-sibling::div/text()").get(),
            'aspect_ratio': response.xpath("//tr/td/div[text()='Aspect Ratio']/following-sibling::div/text()").get(),
            'refresh_rate': response.xpath("//tr/td/div[text()='Refresh Rate']/following-sibling::div/text()").get(),
            'response_time': response_time,
            'panel_type': response.xpath("//tr/td/div[text()='Panel Type']/following-sibling::div/text()").get(),
            'curved_screen': response.xpath("//tr/td/div[text()='Curved Screen']/following-sibling::div/text()").get(),
            'adaptive_sync': adaptive_sync,
            'brightness': response.xpath("//tr/td/div[text()='Brightness']/following-sibling::div/text()").get(),
            'wide_screen': response.xpath("//tr/td/div[text()='Widescreen']/following-sibling::div/text()").get(),
            'viewing_angle': response.xpath("//tr/td/div[text()='Viewing Angle']/following-sibling::div/text()").get(),
            'built_in_speakers': response.xpath("//tr/td/div[text()='Built-in Speakers']/following-sibling::div/text()").get(),
            'input': response.xpath("//tr/td/div[text()='Inputs']/following-sibling::div/text()").get(),
            'vesa_mounting': response.xpath("//tr/td/div[text()='VESA Mounting']/following-sibling::div/text()").get(),
            'hdr_tier': response.xpath("//tr/td/div[text()='HDR Tier']/following-sibling::div/text()").get(),            
        }

