__author__ = 'pascal'
import scrapy
from bs4 import BeautifulSoup

class BerlinGermaniastrTemp(scrapy.Spider):
    name = "berlin_forecast"
    allowed_domains = ["wunderground.com"]
    start_urls = ["http://www.wunderground.com/personal-weather-station/dashboard?ID=IBERLIN725#history"]

    def get_temp(self, soup):
        temp = soup.find("div", {"id": "curTemp"}).find("span", {"class": "wx-value"}).string
        return temp + " C"


    def parse(self, response):

        soup = BeautifulSoup(response.body)
        with open("test.html", "w") as f:
            f.write(response.body)
