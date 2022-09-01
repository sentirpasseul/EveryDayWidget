import requests
import pandas as pd

class GetCoords:
    def __init__(self, city: str):
        self.city = city

        self.get_coords()
        self.get_weather()


    def get_req(self, url):
        req = requests.get(url)
        srs = req.text
        return srs

    def get_coords(self):
        self.url_coords = f'https://geocoding-api.open-meteo.com/v1/search?name={self.city}'
        coords = self.get_req(self.url_coords) # Это строчный тип данных
        print(coords)

        dict_coords = eval(coords) # Преобразование строки в словарь для фильтрации по индексам
        #print(dict_coords)

        self.lat = round(dict_coords['results'][0]['latitude'], 3) # Поиск по индексам
        #print(self.lat)

        self.lon = dict_coords['results'][0]['longitude'] #
        #print(self.lon)

    def get_weather(self):
        self.url_weather = f'https://api.open-meteo.com/v1/forecast?latitude={float(self.lat)}&' \
                           f'longitude={float(self.lon)}&current_weather=True' # api адреса погоды, где берем данные
        req_weather = self.get_req(self.url_weather) # сам запрос данных
        dict_weather = eval(req_weather)['current_weather'] # преобразование строки в словарь
        #print(dict_weather)
        self.temperature = round(dict_weather['temperature']) # Температура в градусах
        if self.temperature > 0:
            self.temperature = f'+{self.temperature}°'
        elif self.temperature < 0:
            self.temperature = f'-{self.temperature}°'
        else:
            self.temperature = f'{self.temperature}°'

        self.wind_speed = dict_weather['windspeed'] # Скорость ветра
        self.wind_direction = dict_weather['winddirection'] # Направление ветра
        self.weather_code = dict_weather['weathercode'] # Код погоды
        print(self.weather_code)

        return self.temperature, int(self.weather_code)



    def save_data(self):
        self.pd_data = pd.DataFrame(
            {
                'Температура': [self.temperature],
                'Скорость ветра': [self.wind_speed],
                'Направление ветра': [self.wind_direction],
                'Код погоды': [self.weather_code]
            }
        )
        print(self.pd_data)




GetCoords('Ulan-Ude')