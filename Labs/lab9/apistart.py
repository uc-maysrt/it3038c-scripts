import json
import requests
print("Please enter your zip code:")
zip = input()
r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=45209,us&appid=ae78ff1de0ef950f6366ecfed5df8ff2' % zip)
data = r.json()
#print(data)
print(data['weather'][0]['description'])
