import requests, re
from bs4 import BeautifulSoup
data = requests.get("https://www.newegg.com/p/N82E16814126456?Item=N82E16814126456").content

soup = BeautifulSoup(data, 'html.parser')
#This pulls the product title
d = soup.find("h1", {"class":"product-title"})
title = d.string.strip()

#This pulls the price of the product
p = soup.find("li", {"class":"price-current"})
price = p.text

#This pulls whether the product is out of stock or not.
span = soup.find("div", {"class":"flags-body has-icon-left fa-exclamation-triangle"})
stock = span.text

#This prints the information.
print("The item '%s' costs %s and is currently %s" % (title, price, stock.lower()))
