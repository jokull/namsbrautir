import json

import scrapy

class NamskraSpider(scrapy.Spider):
    name = 'namskra'
    start_urls = ['https://mms.is/stadfestar-namsbrautalysingar']

    def parse(self, response):
        for link in response.css('.cmp-article a'):
            if link.attrib['href'].startswith('https://namskra.is/programmes'):
                yield response.follow(link.attrib['href'] + '/json', self.parse_course)

    def parse_course(self, response):
        data = json.loads(response.text)
        with open(f'.dumps/{data["_id"]}.json', 'w') as fp:
            fp.write(response.text)
