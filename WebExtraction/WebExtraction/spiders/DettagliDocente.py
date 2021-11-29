import scrapy
import json

class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'dettagliDocenti'
    def start_requests(self):
        f = open('docenti.json')
        data = json.load(f)
        self.start_urls = []
        for i in data:
            start_urls.append('https://www.uniroma3.it' + i['link'])
        print(start_urls)
        return super().start_requests()

    def parse(self, response):
        nome = response.xpath('//*[@id="main"]/h1/text()')
        caratteristiche = response.xpath('//div[@class="boxPersonaDetailsWrap"]/table/tbody/tr/td')
        yield {
            'nome' : nome.extract_first(),
            'qualifica': caratteristiche.xpath('./strong[contains(.,"Qualifica")]/ancestor-or-self::td/following-sibling::td/text()').extract_first(),
            'SSD': caratteristiche.xpath('./strong[contains(.,"Settore Scientifico Disciplinare")]/ancestor-or-self::td/following-sibling::td/text()').extract_first(),
            'email' : caratteristiche.xpath('.//strong[contains(.,"Email")]/ancestor-or-self::td/following-sibling::td/text()').extract_first(),
            }