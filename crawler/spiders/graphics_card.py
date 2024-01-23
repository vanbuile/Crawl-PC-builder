import scrapy
import random
import time


class Graphics_Card_Spider(scrapy.Spider):
    name = "graphics_card"
    def start_requests(self):
        urls = ['https://pc-builder.net/graphics-card/page/']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
        num_pages = 287
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
        displayport_output = response.xpath("//tr/td/div[text()='DisplayPort Outputs']/following-sibling::div/text()").get() \
                            or response.xpath("//tr/td/div[text()='DisplayPort 1.4a Outputs']/following-sibling::div/text()").get() \
                            or response.xpath("//tr/td/div[text()='DisplayPort 1.4 Outputs']/following-sibling::div/text()").get() \
                            or 0
        hdmi_output = response.xpath("//tr/td/div[text()='HDMI Outputs']/following-sibling::div/text()").get() \
                            or response.xpath("//tr/td/div[text()='HDMI 2.1a Outputs']/following-sibling::div/text()").get() \
                            or response.xpath("//tr/td/div[text()='HDMI 2.1 Outputs']/following-sibling::div/text()").get() \
                            or 0
        displayport_ports = response.xpath("//tr/td/div[text()='DisplayPort Ports']/following-sibling::div/text()").get() \
                            or 0
        hdmi_ports = response.xpath("//tr/td/div[text()='HDMI Ports']/following-sibling::div/text()").get() \
                            or 0
        dvi_ports = response.xpath("//tr/td/div[text()='DVI Ports']/following-sibling::div/text()").get() \
                            or 0
        sli_crossfire = response.xpath("//tr/td/div[text()='SLI/CrossFire Support']/following-sibling::div/text()").get() \
                            or "None"
        yield {            
            'name': response.css('h1::text').get(),
            'img': response.css('main div div div img::attr(src)').get(),
            'price': response.css('div.text-4xl::text').get(),
            'manufacturer':response.xpath("//tr/td/div[text()='Manufacturer']/following-sibling::div/text()").get(),
            'part': response.xpath("//tr/td/div[text()='Part #']/following-sibling::div/text()").get(),
            
            #'model': response.xpath("//tr/td/div[text()='Model']/following-sibling::div/text()").get(),
            'chipset': response.xpath("//tr/td/div[text()='Chipset']/following-sibling::div/text()").get(),
            'memory': response.xpath("//tr/td/div[text()='Memory']/following-sibling::div/text()").get(),
            'memory_type': response.xpath("//tr/td/div[text()='Memory Type']/following-sibling::div/text()").get(),
            'core_clock': response.xpath("//tr/td/div[text()='Core Clock']/following-sibling::div/text()").get(),
            'boost_clock': response.xpath("//tr/td/div[text()='Boost Clock']/following-sibling::div/text()").get(),
            'color': response.xpath("//tr/td/div[text()='Color']/following-sibling::div/text()").get(),
            'length': response.xpath("//tr/td/div[text()='Length']/following-sibling::div/text()").get(),
            'tdp': response.xpath("//tr/td/div[text()='TDP']/following-sibling::div/text()").get(),
            'interface': response.xpath("//tr/td/div[text()='Interface']/following-sibling::div/text()").get(),
            'sli_crossfire': sli_crossfire,
            'frame_sync': response.xpath("//tr/td/div[text()='Frame Sync']/following-sibling::div/text()").get(),
            'dvi_ports': dvi_ports,
            'hdmi_ports': hdmi_ports,
            'display_ports': displayport_ports,
            'case_expansion_slot_width': response.xpath("//tr/td/div[text()='Case Expansion Slot Width']/following-sibling::div/text()").get(),
            'total_slot_width': response.xpath("//tr/td/div[text()='Total Slot Width']/following-sibling::div/text()").get(),
            'external_power': response.xpath("//tr/td/div[text()='External Power']/following-sibling::div/text()").get(),
            'cooling': response.xpath("//tr/td/div[text()='Cooling']/following-sibling::div/text()").get(),
            'external_power': response.xpath("//tr/td/div[text()='External Power']/following-sibling::div/text()").get(),
            'display_port_outputs': displayport_output,
            'hdmi_outputs': hdmi_output
        }

