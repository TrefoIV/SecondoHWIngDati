import scrapy

class ValueCompanySpider(scrapy.Spider):
    name = "valueCompanies"
    attributes = ["World Rank (Sep-01-2021)", "Market Cap (Sep-01-2021)", "CEO:", "Company Business", "Number of Employees"]

    def start_requests(self):
        urls= [
            "https://www.value.today/world-top-1000-companies-as-on-jan-2020?field_company_category_primary_target_id=All&field_headquarters_of_company_target_id=All&field_market_value_jan_2020_value=&field_stock_exchange_lc_target_id=All&title=&page=0"
            ]
        for url in urls:
            yield scrapy.Request(url = url, callback=self.parseCompaniesList )

    def format(self, values):
        v = " ".join(values)
        v = v.strip()
        v = v.replace("\n", "")
        v = v.replace("\t", "")
        v = v.replace("\r", "")
        return v

    def parseCompaniesList(self, response):
        
        next_page = response.xpath("//li[@class = 'pager__item pager__item--next']/a/@href")
        next_page = response.urljoin(next_page.get())

        for li in response.xpath("//li[@class='row well']"):
            company_description = {}
            nome = self.format(li.xpath("descendant::h2//text()").getall())
            company_description["name"] = nome
            for attr in self.attributes:
                value = self.format(li.xpath(f"descendant::div[text() = '{attr}']/following-sibling::div//text()").getall())
                company_description[attr.replace(":", "")] = value
            website = self.format(li.xpath(f"descendant::div[text() = 'Company Website:']/following-sibling::div/a/@href").getall())
            company_description["website"] = website
  
            yield company_description

        yield scrapy.Request(url = next_page, callback=self.parseCompaniesList)
        '''
        for a in response.xpath("//ul[@class = 'cl-tree cl-list']/li/descendant::a"):
            print("Here")
            category = a.get()
            print(category)
            link = a.xpath("/@href")
        '''



