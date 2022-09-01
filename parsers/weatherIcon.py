import codecs

from parsers.get_coords import GetCoords
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import *

class WeatherIcon:
    def __init__(self):
        self.get_coords = GetCoords('Ulan-Ude')
        self.degree, self.weather_code = self.get_coords.get_weather()

        #with open('src\weather\codes.json', encoding='utf-8') as file:
         #   self.codes_weather = file.read()


        #item = QGraphicsItem()
        #effect = QGraphicsColorizeEffect()



        self.clouds = QPixmap(r'..\src\icons\cloud_sun.png')
        self.sunny = QPixmap(r'..\src\icons\sunny.png')
        self.rain = QPixmap(r'..\src\icons\rainy.png')



    def get_weather(self):
        icon_w = self.weather_code
        #print('ICON_W', icon_w)

        #if icon_w == 'Clouds' or ('clouds' in icon_w):
        #    return self.rain
        #elif icon_w == 'Rain' or ('rain' in icon_w):
        #    return self.rain
        #elif icon_w == 'Sunny' or ('sunny' in icon_w):
        return self.clouds


