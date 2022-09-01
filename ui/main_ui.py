# -*- coding: utf-8 -*-
import PyQt5.QtGui
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt, QTimer, QTime, pyqtSignal, QSize
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *
from parsers.get_coords import GetCoords
from parsers.get_date import TodayDateTime
from parsers.weatherIcon import WeatherIcon
import sys
import datetime
#from parsers.get_coords import

class MainUi(QWidget):
    updated = pyqtSignal(str, arguments=['time'])
    def __init__(self):
        QWidget.__init__(self)

        self.setWindowFlag(Qt.FramelessWindowHint) #Режим без рамок окна
        self.setAttribute(Qt.WA_TranslucentBackground) #Режим прозрачного фона

        self.city = 'Ulan-Ude'
        self.getCoords = GetCoords(f"{self.city}")
        #weatherIcon = WeatherIcon()
        self.weather_degree, self.weather_icon  = self.getCoords.get_weather()
        #self.path_icon_weather = weatherIcon.get_weather()

        #print(weather_icon, weather_degree)

        self.getDate = TodayDateTime()
        #self.time = self.updateTime()
        self.label_time = QLabel()

        #print('@@@', self.time)

        self.full_day = self.getDate.full_day

        self.initUI()

    def get_time(self):
        today = datetime.datetime.now()
        self.time = (today.strftime("%H:%M:%S"))

        self.label_time.setText(self.time)
        #self.label_time = QLabel(f'{self.time}')  # Текст для отображения времени
        self.label_time.setFont(PyQt5.QtGui.QFont('Inter', 24))  # Изменение шрифта отображения времени
        self.label_time.setStyleSheet('color: white')

    def updateTime(self):
        ...





    def initUI(self):

        #self.updateTime()
        self.timer = QTimer()
        self.timer.start(1000)
        self.timer.timeout.connect(self.get_time)

        label_degree = QtWidgets.QLabel(f"{self.weather_degree}") #Текст для отображения
        label_degree.setFont(PyQt5.QtGui.QFont('Inter', 50)) #Изменение шрифта отображения градусов
        label_degree.setStyleSheet('color: white')

        label_weather = QtWidgets.QLabel()
        label_weather.setText('f')
        #label_icon_weather = QtWidgets.QLabel()              #Инициализация корпуса погоды
        #pixmap_icon_weather = QPixmap(self.path_icon_weather).scaled(90,75) #Иконка погоды с указанием пути к ней
        #pixmap_icon_weather.scaled(90, 75) #Масштабирование иконки погоды
        #label_icon_weather.setPixmap(pixmap_icon_weather) #Добавление иконки в корпус Label
        #label_icon_weather.setStyleSheet('color: white; opacity: 0.72; padding-up: 50px')

        label_city = QtWidgets.QLabel(f'{self.city}') #Текст для отображения города
        label_city.setFont(PyQt5.QtGui.QFont('Inter', 36)) #Изменение шрифта отображения города
        label_city.setStyleSheet('color: white; opacity: 0.72; padding-up: 50px')

        self.time = self.updateTime()
        #self.label_time = QLabel(f'{self.time}')  # Текст для отображения времени
        #self.label_time.setFont(PyQt5.QtGui.QFont('Inter', 24))  # Изменение шрифта отображения времени
        #self.label_time.setStyleSheet('color: white')
        #print('@@@', self.label_time)

        #timer = QTimer()  # creating a timer object
        # timer.setInterval(100)  # установка интервала
        #timer.timeout.connect(self.updateTime)
        #timer.start(1000)  # update the timer every second

        label_date = QtWidgets.QLabel(f'{self.full_day}') #Текст для отображения даты
        label_date.setFont(PyQt5.QtGui.QFont('Inter', 16)) #Изменение шрифта отображения даты
        label_date.setStyleSheet('color: white; padding-left: 30px; padding-down: 50px')

        objects = [f'{label_degree}', f'{label_weather}', f'{label_city}'
                   '9',                  f'{self.label_time}',       f'{label_date}', 'f'] #Как должна выглядеть сетка

        grid = QtWidgets.QGridLayout() # Создание самой сетки

        "Добавление всех labels в сетку"
        grid.addWidget(label_degree, 0, 0)
        grid.addWidget(label_weather, 0, 1)
        grid.addWidget(label_city, 0, 2)
        grid.addWidget(self.label_time, 1, 1)
        grid.addWidget(label_date, 1, 2)

        self.setLayout(grid) #Отображение самой сетки (создание слоя, состоящего из сетки)

        self.move(self.width(), self.height()//6)
        self.setWindowTitle('EveryDayWidget')
        self.show()










if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainUi()
    sys.exit(app.exec_())