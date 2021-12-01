import scrapy
import json

class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'dettagliDocentiBocconi'
    def start_requests(self):
        f = open('docentiBocconi.json')
        data = json.load(f)
        self.start_urls = []
        for i in data:
            self.start_urls.append('https://didattica.unibocconi.it/docenti/' + i['link'])
        #print(start_urls)
        return super().start_requests()

    def parse(self, response):
        
        caratteristiche = response.xpath('//div[@class="txtParagrafo"]//div[@style="margin-bottom:5px;"]/a/text()')
        profProperty = {
            'nome' : response.xpath('//article/div/h1/text()').extract_first(),
            'Dipartimento': response.xpath('//div[@class="txtParagrafo"]//div[@style="margin-bottom:10px; white-space: nowrap;"]/text()').extract_first(),
            'email' : response.xpath('//div[@class="txtParagrafo"]//div[@style="margin-bottom:5px;"]/a/text()').extract_first(),
            }
        
        profProperty['Insegnamenti a.a. 2021/2022'] = []
        for corso in response.xpath('//div[@class="txtParagrafo"]/span/text()'):
            profProperty['Insegnamenti a.a. 2021/2022'].append(corso.get())

        ##profPropertyJson = json.dump(profProperty)
        with open('dettagliDocentiBocconi.json', 'a') as fp:
            json.dump(profProperty, fp)
            fp.write('\n')
        #print(profProperty)
        #yield({profProperty})