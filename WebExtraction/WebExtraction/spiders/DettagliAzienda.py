import scrapy
import json


class QuotesSpider(scrapy.Spider):
    name = 'dettagliAziende'

    def start_requests(self):
        f = open('aziende.json')
        data = json.load(f)
        self.start_urls = []
        for i in data:
            self.start_urls.append('https://companiesmarketcap.com' + i['link'])
            #print(self.start_urls)
        return super().start_requests()

    def parse(self, response):
        #for dettagli in response.xpath('//div[@class="table-container"]'):
            yield {
                'name' : response.xpath('//div[@class="company-title-container"]/div[@class="company-name"]/text()').extract_first(),
                'code' : response.xpath('//div[@class="company-title-container"]/div[@class="company-code"]/text()').extract_first(),
                'country' : response.xpath('//div[@class="col-lg-6"]/div/div/div/a/span/text()').extract_first(),
                'marketcap' : response.xpath('//div[@class="col-lg-6"]/div/div[2]/div[1]/text()').extract_first(),
                'competitor': response.xpath('//table/tbody/*//div[@class="company-name"]/text()').getall(),
            }
