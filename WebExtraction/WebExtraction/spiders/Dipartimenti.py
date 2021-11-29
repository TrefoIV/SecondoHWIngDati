import scrapy
import json

class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'dipartimenti'
    def start_requests(self):
    
        self.start_urls = [
            'https://www.uniroma3.it/en/about-us/departments-and-schools/departments/',
        ]
        return super().start_requests()

    def parse(self, response):
        for dipartimento in response.xpath('//div[@class="list-subpages-container"]/article'):
            yield {
                'nome': dipartimento.xpath('./h3/a/text()').extract_first(),
                'link': dipartimento.xpath('./h3/a/@href').extract_first(),
            }