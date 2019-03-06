import scrapy


class Companies(scrapy.Spider):
    name = 'companies'
    start_urls=[
        'https://www.justdial.com/Delhi/Corporate-Companies'
    ]

    def parse(self,response):
        for company in response.xpath("//span[@class='lng_cont_name']"):
            yield{
                'lng_cont_name': company.xpath(".//span[@class='lng_cont_name']/p").extract_first()

            }

            next_page=response.xpath("//span[@ class='act']/a/@href").extract_first()
            if next_page is not None:
                next_page_link=response.urljoin(next_page)
                yield scrapy.Request(url=next_page_link, callback=self.parse)


