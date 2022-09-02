import codecs

from parsers.get_coords import GetCoords
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *

class WeatherIcon:
    def __init__(self, weather_code):
        self.get_coords = GetCoords('Ulan-Ude')
        self.weather_code = weather_code

        #with open('src\weather\codes.json', encoding='utf-8') as file:
         #   self.codes_weather = file.read()


        #item = QGraphicsItem()
        #effect = QGraphicsColorizeEffect()

        # Импорт иконок погоды
        self.sun = QPixmap(r'..\src\icons\weather\day\sun.png')
        self.sun_clouds = QPixmap(r'..\src\icons\weather\day\cloud_sun.png')
        self.clouds = QPixmap(r'..\src\icons\weather\day\clouds.png')
        self.fog = QPixmap(r'..\src\icons\weather\day\fog.png')
        self.drizzle = QPixmap(r'..\src\icons\weather\day\drizzle.png')
        self.rain = QPixmap(r'..\src\icons\weather\day\rain.png')
        self.snow = QPixmap(r'..\src\icons\weather\day\snow.png')
        self.thunder = QPixmap(r'..\src\icons\weather\day\thunder.png')



    def get_weather(self):
        icon_w = self.weather_code # Получение кода погоды
        #print('ICON_W', icon_w)

        #Списки с кодами погоды
        sun = [0, 1]
        fog = [item for item in range(45, 49)]
        drizzle = [item for item in range(51, 58)]
        rain = [item for item in range(61, 68)]
        snow = [item for item in range(71, 78)]
        rain_showers = [item for item in range(80, 87)]
        snow_showers = [85, 86]
        thunder = ['95 *', 96, '99 *']

        #Условия, при которых код = иконка погоды. Если код = 1, то погода солнечная и отображается иконка солнца
        if icon_w in sun:
            return self.sun
        elif icon_w == 2:
            return self.sun_clouds
        elif icon_w == 3:
            return self.clouds
        elif icon_w in fog:
            return self.fog
        elif icon_w in drizzle:
            return self.drizzle
        elif icon_w in rain:
            return self.rain
        elif icon_w in snow:
            return self.snow
        elif icon_w in rain_showers:
            return self.rain            #!!TODO Сделать для ливней отдельную иконку
        elif icon_w in snow_showers:
            return self.snow            #!!TODO Сделать для снежных ливней отдельную иконку
        elif icon_w in thunder:
            return self.thunder


