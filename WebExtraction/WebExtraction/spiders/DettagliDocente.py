import scrapy
import json

class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'dettagliDocenti'
    f = open('docenti.json')
    data = json.load(f)
    start_urls = []
    for i in data:
        start_urls.append('https://www.uniroma3.it' + i['link'])
    print(start_urls)

    def parse(self, response):
        for docente in response.xpath('//div[@class="boxPersonaDetailsWrap"]/table/tbody'):
            yield {
                'qualifica': docente.xpath('./tr[1]/td[2]/text()').extract_first(),
                'SSD': docente.xpath('./tr[2]/td[2]/text()').extract_first(),
                'email' : docente.xpath('./tr[5]/td[2]/text()').extract_first(),
                #'afferenza' : docente.xpath('./td[contains(.,"Struttura/Afferenza")/following-sibling::td[1]/text()').extract_first(),
            }