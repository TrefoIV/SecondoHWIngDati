import scrapy
import json

class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'docentiR3'

    def start_requests(self):
        f = open('dipartimentiFederico2.json')
        data = json.load(f)
        self.start_urls = []
        for i in data:
            self.start_urls.append(i['link'])
        return super().start_requests()


    def parse(self, response):
        yield scrapy.Request(response.urljoin('roles/PO-PA-RU-SD-RM-RD/'))
        for docenti in response.xpath('//div[@class="entry-content"]/ul/li'):
            yield {
                'nome': docenti.xpath('./a/text()').extract_first(),
                'link': docenti.xpath('./a/@href').extract_first(),
            }
