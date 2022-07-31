# -*- coding: utf-8 -*-
import PyQt5.QtGui
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from parsers.get_coords import GetCoords
from parsers.get_date import TodayDateTime
import sys
#from parsers.get_coords import

class MainUi(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowFlag(Qt.FramelessWindowHint) #Режим без рамок окна
        self.setAttribute(Qt.WA_TranslucentBackground) #Режим прозрачного фона

        self.city = 'Ulan-Ude'
        self.getCoords = GetCoords(f"{self.city}")
        self.weather_degree, self.weather_icon  = self.getCoords.get_coords()
        self.path_icon_weather = "..\src\icons\bi_cloud-sun.png"
        #print(weather_icon, weather_degree)

        self.getDate = TodayDateTime()
        self.time = self.getDate.time
        self.full_day = self.getDate.full_day

        self.initUI()

    def initUI(self):




        label_degree = QtWidgets.QLabel(f"{self.weather_degree}") #Текст для отображения градусов
        label_degree.setFont(PyQt5.QtGui.QFont('Inter', 50)) #Изменение шрифта отображения градусов

        label_icon_weather = QtWidgets.QLabel()
        pixmap_icon_weather = QPixmap(f'{self.path_icon_weather}') #Иконка погоды
        label_icon_weather.setPixmap(pixmap_icon_weather)
        label_icon_weather.resize(90,79)

        label_city = QtWidgets.QLabel(f'{self.city}')
        label_city.setFont(PyQt5.QtGui.QFont('Inter', 36))

        label_time = QtWidgets.QLabel(f'{self.time}')
        label_time.setFont(PyQt5.QtGui.QFont('Inter', 24))

        label_date = QtWidgets.QLabel(f'{self.full_day}')
        label_date.setFont(PyQt5.QtGui.QFont('Inter', 16))

        objects = [f'{label_degree}', f'{label_icon_weather}', f'{label_city}'
                   '9',                  f'{label_time}',       f'{label_date}', 'f']

        positions = [(i, j) for i in range(5) for j in range(4)]

        grid = QtWidgets.QGridLayout()

        grid.addWidget(label_degree, 0, 0)
        grid.addWidget(label_icon_weather, 0, 1)
        grid.addWidget(label_city, 0, 2)
        grid.addWidget(label_time, 1, 1)
        grid.addWidget(label_date, 1, 2)

        self.setLayout(grid)

        self.move(300, 150)
        self.setWindowTitle('EveryDayWidget')
        self.show()





if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MainUi()
    sys.exit(app.exec_())