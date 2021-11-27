import scrapy
import json

class ToScrapeSpiderXPath(scrapy.Spider):
    name = 'professori'
    f = open('nomi.json')
    data = json.load(f)
    start_urls = []
    for i in data:
        start_urls.append(i['link'])


    def parse(self, response):
        yield scrapy.Request(response.urljoin('roles/PO-PA-RU-SD-RM-RD/'))
        for professori in response.xpath('//div[@class="entry-content"]/ul/li'):
            yield {
                'nome': professori.xpath('./a/text()').extract_first(),
                'link': professori.xpath('./a/@href').extract_first(),
            }
