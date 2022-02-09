import scrapy
from ..items import QuoteItem


class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://www.mytheresa.com/int_en/men/shoes.html'
    ]

    def parse(self, response, **kwargs):

        items = QuoteItem()

        all_new_arrival = response.css('li.item')

        for lst in all_new_arrival:
            product_designer = lst.css('.ph1::text').extract()
            product_name = lst.css('.pa1-rm::text').extract()
            product_price = lst.css('.special-price .price::text').extract()
            product_old_price = lst.css('.old-price .price::text').extract()

            items['product_designer'] = product_designer
            items['product_name'] = product_name
            items['product_price'] = product_price
            items['product_old_price'] = product_old_price

            yield items



