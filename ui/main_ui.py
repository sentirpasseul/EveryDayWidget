# -*- coding: utf-8 -*-
import PyQt5.QtGui
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *
from parsers.get_coords import GetCoords
from parsers.get_date import TodayDateTime
from parsers.weatherIcon import WeatherIcon
import sys
#from parsers.get_coords import

class MainUi(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowFlag(Qt.FramelessWindowHint) #Режим без рамок окна
        self.setAttribute(Qt.WA_TranslucentBackground) #Режим прозрачного фона

        self.city = 'Ulan-Ude'
        self.getCoords = GetCoords(f"{self.city}")
        weatherIcon = WeatherIcon()
        self.weather_degree, self.weather_icon  = self.getCoords.get_coords()
        self.path_icon_weather = weatherIcon.get_weather()
        #print(weather_icon, weather_degree)

        self.getDate = TodayDateTime()
        self.time = self.getDate.time
        self.full_day = self.getDate.full_day

        self.initUI()

    def initUI(self):

        label_degree = QtWidgets.QLabel(f"{self.weather_degree}") #Текст для отображения
        label_degree.setFont(PyQt5.QtGui.QFont('Inter', 50)) #Изменение шрифта отображения градусов
        label_degree.setStyleSheet('color: white')

        label_icon_weather = QtWidgets.QLabel()              #Инициализация корпуса погоды
        pixmap_icon_weather = QPixmap(self.path_icon_weather) #Иконка погоды с указанием пути к ней
        label_icon_weather.setPixmap(pixmap_icon_weather) #Добавление иконки в корпус Label
        label_icon_weather.resize(90,79) # изменение размеров иконки

        label_city = QtWidgets.QLabel(f'{self.city}') #Текст для отображения города
        label_city.setFont(PyQt5.QtGui.QFont('Inter', 36)) #Изменение шрифта отображения города
        label_city.setStyleSheet('color: white; padding-up: 50px')

        label_time = QtWidgets.QLabel(f'{self.time}') #Текст для отображения времени
        label_time.setFont(PyQt5.QtGui.QFont('Inter', 24)) #Изменение шрифта отображения времени
        label_time.setStyleSheet('color: white')

        label_date = QtWidgets.QLabel(f'{self.full_day}') #Текст для отображения даты
        label_date.setFont(PyQt5.QtGui.QFont('Inter', 16)) #Изменение шрифта отображения даты
        label_date.setStyleSheet('color: white; padding-left: 30px; padding-down: 50px')

        objects = [f'{label_degree}', f'{pixmap_icon_weather}', f'{label_city}'
                   '9',                  f'{label_time}',       f'{label_date}', 'f'] #Как должна выглядеть сетка

        grid = QtWidgets.QGridLayout() # Создание самой сетки

        "Добавление всех labels в сетку"
        grid.addWidget(label_degree, 0, 0)
        grid.addWidget(label_icon_weather, 0, 1)
        grid.addWidget(label_city, 0, 2)
        grid.addWidget(label_time, 1, 1)
        grid.addWidget(label_date, 1, 2)

        self.setLayout(grid) #Отображение самой сетки (создание слоя, состоящего из сетки)

        self.move(self.width(), self.height()//6)
        self.setWindowTitle('EveryDayWidget')
        self.show()





if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MainUi()
    sys.exit(app.exec_())