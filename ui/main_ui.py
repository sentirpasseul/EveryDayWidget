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
        weatherIcon = WeatherIcon()
        self.weather_degree, self.weather_icon  = self.getCoords.get_weather()
        self.path_icon_weather = weatherIcon.get_weather()

        #print(weather_icon, weather_degree)

        self.getDate = TodayDateTime()
        #self.time = self.updateTime()
        self.label_time = QLabel()
        self.label_date = QLabel()
        self.label_degree = QLabel()
        self.label_degree.setText(self.weather_degree)  # Текст для отображения
        self.label_degree.setFont(PyQt5.QtGui.QFont('Inter', 36))  # Изменение шрифта отображения градусов
        self.label_degree.setStyleSheet('color: white')

        #print('@@@', self.time)

        self.full_day = self.getDate.full_day

        self.initUI()

    def update_time(self):
        today = datetime.datetime.now()
        self.time = (today.strftime("%H:%M"))

        self.label_time.setText(self.time)
        #self.label_time = QLabel(f'{self.time}')  # Текст для отображения времени
        self.label_time.setFont(PyQt5.QtGui.QFont('Inter', 24))  # Изменение шрифта отображения времени
        self.label_time.setStyleSheet('color: white; ')

        self.label_date.setText(self.full_day)  # Текст для отображения даты
        self.label_date.setFont(PyQt5.QtGui.QFont('Inter', 16))  # Изменение шрифта отображения даты
        self.label_date.setStyleSheet('color: white; padding-left: 10px; padding-down: 50px')

    def update_weather(self):
        self.label_degree.setText(self.weather_degree)  # Текст для отображения
        self.label_degree.setFont(PyQt5.QtGui.QFont('Inter', 36))  # Изменение шрифта отображения градусов
        self.label_degree.setStyleSheet('color: white')


    def initUI(self):

        #self.updateTime()
        self.timer_time = QTimer()
        self.timer_time.start(250)
        self.timer_time.timeout.connect(self.update_time)

        self.timer_weather = QTimer()
        self.timer_weather.start(600000)
        self.timer_weather.timeout.connect(self.update_weather)






        #label_weather = QtWidgets.QLabel()
        #label_weather.setText('f')
        label_icon_weather = QtWidgets.QLabel()              #Инициализация корпуса погоды
        pixmap_icon_weather = QPixmap(self.path_icon_weather) #Иконка погоды с указанием пути к ней
        pixmap_icon_weather.scaled(90, 90) #Масштабирование иконки погоды
        label_icon_weather.setPixmap(pixmap_icon_weather) #Добавление иконки в корпус Label
        label_icon_weather.setStyleSheet('color: white; opacity: 0.72; margin-left: 10px')

        label_city = QtWidgets.QLabel(f'{self.city}') #Текст для отображения города
        label_city.setFont(PyQt5.QtGui.QFont('Inter', 36)) #Изменение шрифта отображения города
        label_city.setStyleSheet('color: white; opacity: 0.72; padding-up: 50px')

        grid = QtWidgets.QGridLayout() # Создание самой сетки

        "Добавление всех labels в сетку"
        grid.addWidget(self.label_degree, 0, 0)
        grid.addWidget(label_icon_weather, 0, 1)
        grid.addWidget(label_city, 0, 2)
        grid.addWidget(self.label_time, 1, 1)
        grid.addWidget(self.label_date, 1, 2)

        self.setLayout(grid) #Отображение самой сетки (создание слоя, состоящего из сетки)

        self.move(self.width(), self.height()//6)
        self.setWindowTitle('EveryDayWidget')
        self.show()










if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainUi()
    sys.exit(app.exec_())