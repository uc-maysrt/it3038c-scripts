import requests, re
from bs4 import BeautifulSoup
#This one is currently sold out.
#data = requests.get("https://www.microcenter.com/product/630684/asus-geforce-rtx-3070-tuf-overclocked-triple-fan-8gb-gddr6-pcie-40-graphics-card").content

#This one has 1 in stock as of Sunday 3/21 1900 EDT
#data = requests.get("https://www.microcenter.com/product/634208/amd-ryzen-threadripper-pro-3995wx-castle-peak-27ghz-64-core-swrx8-boxed-processor").content

#this would allow the user to paste in a specific page to check current stock.
print("Enter a microcenter webpage:")
site = input()
data = requests.get(site).content

soup = BeautifulSoup(data, 'html.parser')
#This pulls the product title
#non-regex ways:
#(does not work with any product on Microcenter's site)
#d = soup.find("span", {"class":"ProductLink_630684"})
#d = soup.find("span", {"class":"ProductLink_634208"})

#regex way:
# "should" work with any product on Microcenter's site
# Apparently it works with *almost* everything except prebuilt Desktops, Laptops, and smart phones.
# Presumably it is because the product name is on the top and the specs are on the bottom.
# Also does not work on pages with multiple prices due to volume discounts such as:
# https://www.microcenter.com/product/484619/eset-internet-security---1-device,-3-year-(oem)

d = soup.find("span", {"class":re.compile('(ProductLink_)[0-9]')})
title = d.string.strip()

#This pulls the price of the product
p = soup.find("span", {"id":"pricing"})
price = p.text

#This pulls whether the product is out of stock or not.
s = soup.find("span", {"class":"inventoryCnt"})
stock = s.text
 
#This prints the information.
print("The item '%s' costs %s and is currently %s" % (title, price, stock.lower()))
