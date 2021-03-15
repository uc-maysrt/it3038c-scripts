import requests, re
from bs4 import BeautifulSoup
#r = requests.get("http://webscraper.io/test-sites/e-commerce/allinone/phones").content
#soup = BeautifulSoup(r, "lxml")
#tags = soup.findAll("a", {"href":re.compile('(allinone)')})
#tags = soup.findAll("a", {"href":re.compile('[<>#%|\{\}!\\^~\[\]`/]')})
#for a in tags:
#    print(a.get('href'))
#tags = soup.findAll("div", {"class":re.compile('(ratings)')})
#for p in tags:
#    a = p.findAll("p", {"class": "pull-right"})
#    print(a[0].string)
data = requests.get("https://www.reebok.com/us/flexagon-energy-shoes---preschool/DV8354.html").content
soup = BeautifulSoup(data, 'html.parser')
span = soup.find("h1", {"class": "product_information_title__value--sale"})
price = span.text
print("Item %s has price %s" %(title, price))