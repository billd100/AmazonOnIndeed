# -*- coding: utf-8 -*-
import scrapy


class AmazonOnIndeed(scrapy.Spider):
    name = 'AmazonOnIndeed'
    allowed_domains = ['https://www.indeed.com']
    start_urls = ['https://www.indeed.com/jobs?q=amazon']

    def parse(self, response):
        for listing in response.css('div.row.result'):

            # the company on Indeed is in format: "<b>First</b>\n Last"
            # grab elements, extract
            companyNameList = listing.css('span[itemprop="name"] > a > b::text').extract() + listing.css('span[itemprop="name"] > a::text').extract()

            # concatenate the list elements into single string
            companyName = "".join(companyNameList)
            yield {
                'title': listing.css('h2 > a.turnstileLink::text').extract_first(),
                'company': companyName,
                'location': listing.css('span[itemprop="addressLocality"]::text').extract_first(),
            }
