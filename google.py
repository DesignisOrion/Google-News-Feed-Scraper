# Author: Orion Ford
# This app will allow you to scrape the Google News feed. Enjoy.

import bs4  # importing BeautifulSoup
# importing beautifulsoup declariing it as soup
from bs4 import BeautifulSoup as soup
# stating from the urllib3 request, use the urlopen feature.
from urllib.request import urlopen


news_url = "https://news.google.com/news/rss"
Client = urlopen(news_url)  # this is how you fetch the package
xml_page = Client.read()  # declare the xml which is produced by feed.
Client.close()  # close the connection of the news feed at that moment
soup_page = soup(xml_page, "xml")
news_list = soup_page.findAll("item")

# This is where you will bprint the news title, url and publish date :)
for news in news_list:
    print(news.title.text)
    print(news.link.text)
    print(news.pubDate.text)
    print("_"*60)
