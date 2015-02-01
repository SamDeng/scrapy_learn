from scrapy.spider import BaseSpider


class demo(BaseSpider):
    name = "dmoz"
    allow_domain = ["dmoz.org"]
