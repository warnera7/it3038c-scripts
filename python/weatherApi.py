import json
from pprint import PrettyPrinter
import requests

print('Please enter your zip code: ')
zip = input()

r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=%s,us&appid=713f19b84037f6c7c810bc63553459c1' % zip)
data = r.json()

#print(data['weather'])
print(data['weather'][0]['description'])