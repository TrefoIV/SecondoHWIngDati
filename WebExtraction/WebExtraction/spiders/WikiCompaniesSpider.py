import scrapy
from unicodedata import normalize
import re


class WikiCompaniesSpider(scrapy.Spider):
    name = "wikiCompanies"

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

            for hrefSelector in span.xpath("following::small[1]/a/@href"):
                link = response.urljoin(hrefSelector.get())
                yield scrapy.Request(url = "https://en.wikipedia.org/wiki/Qantas", callback = self.parseCompany, cb_kwargs = {"industrial_sector" : industrial_sector})
                break
            break

    def parseCompany(self, response, industrial_sector):
        attributes = ["Founded", "Revenue"]
        for attr in attributes:
            #row  = response.xpath(f"//tr/descendant::*[text() = '{attr}']")
            #row = row.xpath("parent::tr/td")
            #response.xpath("//tr/descendant::*[text() = 'Founded']/parent::tr/td")
            attr_value = ""
            for text in response.xpath(f"//tr/descendant::*[text() = '{attr}']/ancestor::tr/td//text()"):
                stringa = text.get()
                stringa = normalize("NFKC", stringa )    #Trasforma eventuali caratteri speciali unicode contenuti nel testo
                stringa = re.sub("\[[1-9]*\]", "", stringa) #Rimuove eventuali riferimenti a fonti di wikipedia
                print(stringa)
                attr_value += stringa
                print(attr_value)
            print(f"{attr} : {attr_value}")

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')




