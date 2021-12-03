import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'aziende'
    start_urls = [
        'https://companiesmarketcap.com/',
    ]

    def parse(self, response):
        for azienda in response.xpath('//table[@class="table marketcap-table dataTable"]/tbody/tr'):
            yield {
                'name' : azienda.xpath('./td[@class="name-td"]/div[@class="name-div"]/a/div[@class="company-name"]/text()').extract_first(),
                'link' : azienda.xpath('./td[@class="name-td"]/div[@class="name-div"]/a/@href').extract_first(),
            }
        next_page = response.xpath('//li[@class="page-item"]/a[last()]/@href').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
