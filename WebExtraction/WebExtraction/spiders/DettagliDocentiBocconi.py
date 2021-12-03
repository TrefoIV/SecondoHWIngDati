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
        
        #caratteristiche = response.xpath('//div[@class="txtParagrafo"]//div[@style="margin-bottom:5px;"]/a/text()')
        #@style="margin-bottom:10px; white-space: nowrap;"
        #@style="margin-bottom:5px;"
        profProperty = {
            'nome' : response.xpath('//article/div/h1/text()').extract_first(),
            'qualifica' : response.xpath('//div[@class="txtParagrafo"]//div[1]/text()').extract_first(),
            'dipartimento': response.xpath('//div[@class="txtParagrafo"]//div[2]/text()').extract(),
            'email' : response.xpath('//div[@class="txtParagrafo"]//div[3]/a/text()').extract_first(),
            }
        
        #profProperty['dipartimento'] = self.clean(profProperty['dipartimento'])
        #print(profProperty['dipartimento'])
        profProperty['dipartimento'] = ' '.join(profProperty['dipartimento'])
        #print(profProperty['dipartimento'])
        profProperty['dipartimento'] = self.clean(profProperty['dipartimento'])
        #print(profProperty['dipartimento'])
        
        profProperty['corsi'] = []
        for corso in response.xpath('//div[@class="txtParagrafo"]/span/text()'):
            profProperty['corsi'].append(corso.get())

        ##profPropertyJson = json.dump(profProperty)
        #with open('dettagliDocentiBocconi.json', 'a') as fp:
        #    json.dump(profProperty, fp)
        #    fp.write('\n')
        #print(profProperty)
        yield profProperty


    def clean(self, stringa):
        stringa = stringa.strip()
        stringa = stringa.replace("'\r\n\t'", "")
        stringa = stringa.replace("'\t'", "")
        #stringa = re.sub("\[[1-9]*\]", "", stringa)     #Rimuove eventuali riferimenti a fonti di wikipedia
        return stringa