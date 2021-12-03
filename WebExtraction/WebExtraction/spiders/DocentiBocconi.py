import scrapy
import json

class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'docentiBocconi'

    def start_requests(self):
    
        self.start_urls = [
            'https://didattica.unibocconi.it/docenti/proff_ord_alfa.php',
        ]
        return super().start_requests()

    def parse(self, response):
        for dipartimento in response.xpath('//div[@class="txtParagrafo"]/div[@style="border-bottom: 1px solid #cccccc; font-size:12px; padding:10px;"]/a'):
            yield {
                'nome': dipartimento.xpath('./text()').extract_first(),
                'link': dipartimento.xpath('./@href').extract_first(),
            }
