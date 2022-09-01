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


        self.sun = QPixmap(r'..\src\icons\weather\day\sun.png')
        self.sun_clouds = QPixmap(r'..\src\icons\weather\day\cloud_sun.png')
        self.clouds = QPixmap(r'..\src\icons\weather\day\clouds.png')
        self.fog = QPixmap(r'..\src\icons\weather\day\fog.png')
        self.rain = QPixmap(r'..\src\icons\weather\day\rain.png')
        self.snow = QPixmap(r'..\src\icons\weather\day\snow.png')
        self.thunder = QPixmap(r'..\src\icons\weather\day\thunder.png')



    def get_weather(self):
        icon_w = self.weather_code
        #print('ICON_W', icon_w)

        #if icon_w == 'Clouds' or ('clouds' in icon_w):
        #    return self.rain
        #elif icon_w == 'Rain' or ('rain' in icon_w):
        #    return self.rain
        #elif icon_w == 'Sunny' or ('sunny' in icon_w):
        return self.clouds


