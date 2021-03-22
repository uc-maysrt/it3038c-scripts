import requests, re
from bs4 import BeautifulSoup
#Reebok does not actually work.
#data = requests.get("https://www.reebok.com/us/flexagon-energy-shoes---preschool/DV8354.html").content
#soup = BeautifulSoup(data, 'html.parser')
#span = soup.find("h1", {"class": "product_information_title___2rG9M product_title g1-heading g1-heading--m"})
#title = span.text
#span = soup.find("h1", {"class": "gl-price__valueproduct_information_title__value--sale"})
#price = span.text
#print("Item %s has price %s" %(title, price))
data = requests.get("https://shop.funimation.com/home-video/attack-on-titan-complete-season-3/BLR-00721.html").content
#print(data)
#d = soup.find("h2", {"class":re.compile("c-heading-4")})
#print(d.string)
soup = BeautifulSoup(data, 'html.parser')
d = soup.find("div", {"class":"product-name"})
title = d.string.strip()
p = soup.find("span", {"class":"value"})
price = p.get('content').strip()
print("The item '%s' costs $%s" % (title, price))