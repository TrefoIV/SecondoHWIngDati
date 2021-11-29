
import scrapy


class QuotesSpider(scrapy.Spider):
    name = "porco"

    def start_requests(self):
        urls = [
            'https://en.wikipedia.org/wiki/Portal:Companies/Index_by_industry'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parseCompaniesIndex)

    def parseCompaniesIndex(self, response):
        for span in response.xpath("//span[@class='flagicon']"):
            industrial_sector = span.xpath("normalize-space(../../div/descendant::b/a/text())").get()
            if industrial_sector == "":
                industrial_sector = span.xpath("normalize-space(../../p/b/a/text())").get()
            print("===============================================================")
            print(span.xpath("following"))
            print("================================================================")
            for porco in span.xpath("following"):
                print("Ciao")
                print(porco)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')




