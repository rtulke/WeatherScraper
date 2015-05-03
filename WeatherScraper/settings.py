# -*- coding: utf-8 -*-

# Scrapy settings for WeatherScraper project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'WeatherScraper'

SPIDER_MODULES = ['WeatherScraper.spiders']
NEWSPIDER_MODULE = 'WeatherScraper.spiders'
LOG_LEVEL = "ERROR"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'WeatherScraper (+http://www.yourdomain.com)'
