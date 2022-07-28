import requests
from bs4 import BeautifulSoup

url = 'https://www.gismeteo.ru/weather-ulan-ude-4804/'

headers = {
    "accept": "*/*",
"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
(KHTML, like Gecko) Chrome/102.0.5005.134 YaBrowser/22.7.1.806 Yowser/2.5 Safari/537.36'
}

req = requests.get(url, headers=headers)
src = req.text
# print(src)
with open('index.html', 'w') as file:
    file.write(src)