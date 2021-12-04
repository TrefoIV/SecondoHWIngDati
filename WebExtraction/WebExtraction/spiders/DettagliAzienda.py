import scrapy
import json


class QuotesSpider(scrapy.Spider):
    name = 'dettagliAziende'
    total = 0
    valNulli={"name":0,"code":0,"rank":0,"country":0,"marketcap":0,"competitor":0}


    def start_requests(self):
        f = open('aziende.json', encoding="utf8")
        data = json.load(f)
        self.start_urls = []
        for i in data:
            self.start_urls.append('https://companiesmarketcap.com' + i['link'])
            #print(self.start_urls)
        return super().start_requests()

    def parse(self, response):

        proprieta={
        'name' : response.xpath('//div[@class="company-title-container"]/div[@class="company-name"]/text()').extract_first(),
        'code' : response.xpath('//div[@class="company-title-container"]/div[@class="company-code"]/text()').extract_first(),
        'rank' : response.xpath('//div[@class="col-lg-6"]/div[1]/div[1]/div[1]/text()').extract_first().replace("#",""),
        'country' : response.xpath('//div[@class="col-lg-6"]/div/div/div/a/span/text()').extract_first(),
        'marketcap' : response.xpath('//div[@class="col-lg-6"]/div/div[2]/div[1]/text()').extract_first(),
        'competitor' : response.xpath('//table/tbody/*//div[@class="company-name"]/text()').getall()
        }

        yield proprieta

        for attributo in proprieta:
            if(proprieta[attributo]=="" or proprieta[attributo]==[]):
                self.total += 1
                self.valNulli[attributo] += 1

    def closed(self, reason):
        print("--- Valori nulli : ", self.total)
        for attributo in self.valNulli.keys():
            print("--- Valori nulli per", attributo, ":", self.valNulli[attributo])
