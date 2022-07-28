import gzip

import requests
import json
import re
from bs4 import BeautifulSoup
import numpy as np


class GetCoords:

    def __init__(self, city: str):
        self.city = city
        self.appid = '353a92b5518119c1c1cdad7cc0ab9e41'
        self.url_coords = f"https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={self.appid}"
        self.kelvin = 273.15

    def get_req(self, url: str):
        req = requests.get(url)
        srs = req.text
        return srs

    def get_coords(self):
        srs_coords = self.get_req(self.url_coords)
        dict_coords = eval(srs_coords) # конвертация в словарь
        print('Получаемые данные из местности:', dict_coords)
        lon = round(dict_coords['coord']['lon'])
        lat = round(dict_coords['coord']['lat'])
        print("Широта:", lat, "Долгота:", lon)

        weather_air = dict_coords['weather'][0]['main']

        weather_current = round(dict_coords['main']['feels_like'] - self.kelvin)
        #Если погода меньше 0, то добавляется перед числом знак "-", если больше - знак "+"
        if weather_current > 0:
            weather_current = f'+{weather_current}°'
        elif weather_current < 0:
            weather_current = f'-{weather_current}°'
        else:
            weather_current = f'{weather_current}°'

        print("Иконка погоды:",weather_air)
        print('Погода сейчас: ', weather_current)
        #print(dict_coords['weather'])

        with open('coords/coords_city.json', 'w', encoding='utf-8') as file:
            file.write(srs_coords)
        return lat, lon

    def get_weather(self):
        lon, lat = self.get_coords()
        url_weather = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={self.appid}'
        #with gzip.open('data_weather/daily_16.json.gz', 'rt', encoding='UTF-8') as zipfile:
         #   data = json.load(zipfile)
        srs_weather = self.get_req(url_weather)
        self.dict_weather = eval(srs_weather)
        #print("Погода: ",self.dict_weather)


    def __del__(self):
        ...






coords = GetCoords(city='Ulan-Ude')
coords.get_weather()