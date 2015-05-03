__author__ = 'pascal'
import scrapy
from bs4 import BeautifulSoup

class Wetter24(scrapy.Spider):
    name = "wetter24"
    allowed_domains = ["wetter24.de"]
    start_urls = ["http://www.wetter24.de/vorhersage/7tage/deutschland/12099/16156188/"]


    def get_rain_prob(self, soup):
        table = soup.find("table", {"class": "forecast_details_02"})
        td = table.find_all("td")
        return td[34].text

    def get_sunshine_length(self,soup):
        table = soup.find("table", {"class": "forecast_details_02"})
        td = table.find_all("td")
        return td[17].text

    def parse(self, response):
        soup = BeautifulSoup(response.body)
        with open("berlin_rain_prob", "w") as f:
            f.write(self.get_rain_prob(soup))
        with open("berlin_sunshine_length", "w") as f:
            f.write(self.get_sunshine_length(soup))
