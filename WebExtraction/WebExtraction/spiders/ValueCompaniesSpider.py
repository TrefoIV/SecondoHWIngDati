import scrapy

class ValueCompanySpider(scrapy.Spider):
    name = "valueCompanies"
    attributes = ["World Rank (Sep-01-2021)", "Market Cap (Sep-01-2021)", "Market Value (Jan-01-2021)", "CEO:", "Company Business", "Number of Employees", "Annual Revenue in USD", "Annual Net Income in USD", "Annual Results for Year Ending", "Founded Year", "Headquarters Country"]
    attr_dict_key = {
        "World Rank (Sep-01-2021)" : "rank",
        "Market Cap (Sep-01-2021)" : "marketcap",
        "Market Value (Jan-01-2021)": "market value",
        "CEO:" : "ceo",
        "Company Business" : "business",
        "Number of Employees" : "employees",
        "Annual Revenue in USD": "annual revenue",
        "Annual Net Income in USD" : "annual net income in usd",
        "Annual Results for Year Ending" : "annual result for year ending",
        "Founded Year" : "founded year",
        "Headquarters Country":"country"}

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

    def mapAttr(self, attr):
        return self.attr_dict_key[attr]

    def parseCompaniesList(self, response):
        
        next_page = response.xpath("//li[@class = 'pager__item pager__item--next']/a/@href")
        next_page = response.urljoin(next_page.get())

        for li in response.xpath("//li[@class='row well']"):
            company_description = {}
            page_link = "https://value.today" + self.format(li.xpath("descendant::h2//@href").getall())
            
  
            yield scrapy.Request(url = page_link, callback=self.parseCompany)

        yield scrapy.Request(url = next_page, callback=self.parseCompaniesList)
        
    def parseCompany(self, response):
        company_description = {}
        nome = self.format(response.xpath("//h1[@class='clearfix col-sm-12']//text()").getall())
        company_description["name"] = nome
        for attr in self.attributes:
            value = self.format(response.xpath(f"//div[text() = '{attr}']/following-sibling::div//text()").getall())
            company_description[self.mapAttr(attr)] = value
        company_description["founders"] = ""
        for founder in response.xpath(f"//div[text() = 'Founders']/following-sibling::div//text()"):
            company_description["founders"] += f"{self.format(founder.getall())} "
        website = self.format(response.xpath(f"//div[text() = 'Company Website:']/following-sibling::div//@href").getall())
        company_description["website"] = website
        yield company_description




