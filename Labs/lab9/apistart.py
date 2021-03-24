import json
import requests
print("Please enter your zip code:")
zip = input()
r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=%s,us&appid=<API KEY SHOULD BE HERE>' % zip)
#
data = r.json()
print(data)
print(data['weather'][0]['description'])

#dictionaries are in { } and use key value pairs
#lists are in [ ] and use numeric indexes/indicies [0-n]