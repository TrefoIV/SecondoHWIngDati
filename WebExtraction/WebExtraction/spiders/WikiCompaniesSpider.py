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

            for index, hrefSelector in enumerate(span.xpath("following::small[1]/a/@href")):
                name = span.xpath(f"following::small[1]/a[{index+1}]/text()").get()
                link = response.urljoin(hrefSelector.get())
                yield scrapy.Request(url = link, callback = self.parseCompany, cb_kwargs = {"industrial_sector" : industrial_sector, "name" : name})
            

    def parseCompany(self, response, industrial_sector, name):
        attributes = ["Founded", "Revenue", "Key people", "Headquarters", "Total assets", "Employees", "Number of employees", "Website", "Hubs"]
        company_description = {
            "name" : name,
            "industrial_sector" : industrial_sector
        }

        for attr in attributes:          
            attr_value = ""
            list_attr = response.xpath(f"//tr/descendant::*[text() = '{attr}']/ancestor::tr//ul") != []
            if list_attr:
                attr_value = []
                for li in response.xpath(f"//tr/descendant::*[text() = '{attr}']/ancestor::tr//ul/li"):
                    attr_value.append(self.buildAttribute(li))
            else:
                td = response.xpath(f"//tr/descendant::*[text() = '{attr}']/ancestor::tr/td")
                attr_value += self.buildAttribute(td)

            if attr_value == "" or attr_value == []:    #L'attributo non ha valori, metto un valore nullo
                attr_value = None
            
            company_description[attr] = attr_value
        yield company_description

    def buildAttribute(self, node):
        attr_value = ""
        for text in node.xpath(f"descendant-or-self::*//text()"):
            stringa = text.get()
            stringa = normalize("NFKC", stringa )    #Trasforma eventuali caratteri speciali unicode contenuti nel testo
            stringa = re.sub("\[[1-9]*\]", "", stringa) #Rimuove eventuali riferimenti a fonti di wikipedia
            attr_value += stringa
        return attr_value

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log(f'Saved file {filename}')




