import scrapy

startURL = 'https://www.foodpantries.org/st/oklahoma'

class FoodPantrySpider(scrapy.Spider):
    name = "fp"
    start_urls = [
        startURL
    ]

    def parse(self, response):
        yield from response.follow_all(response.css('td a'), self.parseJSON)

    def parseJSON(self, response):
        yield {
            'data': response.xpath('//script[contains(., "context")]/text()').getall()
        }

