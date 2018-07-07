# -*- coding: utf-8 -*-
import scrapy


class ZomatoSpider(scrapy.Spider):
    name = 'zomato'
    allowed_domains = ['foursquare.com']
    start_urls = [
        'https://foursquare.com/explore?cat=food&mode=url&near=Jaipur%2C%20Rajasthan%2C%20India&nearGeoId=72057594039197451',
        
    ]


    def parse(self, response):
        alldata = []
        comments = []
        li = []
        print("response")
        alldata =response.css('a::text').extract()
        comments = response.css('a.userName::text').extract()
        venue = list(set(alldata).difference(comments)) # a tag has both commentors and cafe name
        
        venue = response.xpath("//ul/li[position()>=1 and position()<=30]/div[2]/div[1]/div[1]/div/div[1]/h2/a/text()").extract()
        rating = response.xpath("//ul/li[position()>=1 and position()<=30]/div[2]/div[1]/div[1]/div/div[2]/div[1]/text()").extract()
        address = response.xpath("///ul/li[position()>=1 and position()<=30]/div[2]/div[1]/div[1]/div/div[2]/div[2]/div[1]/text()").extract()
        rtype = response.xpath("//ul/li[position()>=1 and position()<=30]/div[2]/div[1]/div[1]/div/div[2]/div[2]/div[2]/span[1]/span[1]/text()").extract()
        date = response.xpath("//ul/li[position()>=1 and position()<=30]/div[2]/div[1]/div[2]/ul/li/p/span[1]/text()").extract()
        author = response.xpath("//ul/li[position()>=1 and position()<=30]/div[2]/div[1]/div[2]/ul/li/p/span[1]/a/text()").extract()
        location = response.css("div.venueName > h2 > a::attr(href)").extract()

        item = {
                "venue":venue,
                "rating":rating,
                "address":address,
                "rtype":rtype,
                "date":date,
                "author":author,
                "location":location    
                }
        yield item



        #scrapy runspider zomato.py -o data.json



