import scrapy
import json

class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'dettagliDocentiR3'
    def start_requests(self):
        f = open('docentiR3.json')
        data = json.load(f)
        self.start_urls = []
        for i in data:
            self.start_urls.append('https://www.uniroma3.it' + i['link'] +'/insegnamenti/')
        #print(start_urls)
        return super().start_requests()

    def parse(self, response):
        nome = response.xpath('//*[@id="main"]/h1/text()')
        caratteristiche = response.xpath('//div[@class="boxPersonaDetailsWrap"]/table/tbody/tr/td')
        profProperty = {
            'nome' : nome.extract_first(),
            'qualifica': caratteristiche.xpath('./strong[contains(.,"Qualifica")]/ancestor-or-self::td/following-sibling::td/text()').extract_first(),
            'SSD': caratteristiche.xpath('./strong[contains(.,"Settore Scientifico Disciplinare")]/ancestor-or-self::td/following-sibling::td/text()').extract_first(),
            'email' : caratteristiche.xpath('.//strong[contains(.,"Email")]/ancestor-or-self::td/following-sibling::td/text()').extract_first(),
            'email' : caratteristiche.xpath('./strong[contains(.,"Email")]/ancestor-or-self::td/following-sibling::td/text()').extract_first(),
            'link al curriculum' : caratteristiche.xpath('./a[contains(.,"Curriculum")]/@href').extract_first(),
            }
     
        
        
        profProperty['corsi'] = []
        for corso in response.xpath('//main[@id="main"]/h2[1]/following-sibling::strong/text()'):
            profProperty['corsi'].append(corso.get())

        yield profProperty
        ###profPropertyJson = json.dump(profProperty)
        #with open('dettagliDocentiR3.json', 'a') as fp:
        #    json.dump(profProperty, fp)
        #    fp.write(',\n')
        ##print(profProperty)
        ##yield({profProperty})