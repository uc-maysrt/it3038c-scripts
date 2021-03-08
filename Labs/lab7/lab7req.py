import requests
target = requests.get('https://www.uc.edu')
target.status_code
target.encoding
#target.text
targetScrape = open('uc_homepage.html', 'w')
print(target.text, file = targetScrape)
targetScrape.close()