# -*- coding: utf-8 -*-
import PyQt5.QtGui
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt, QTimer, QTime, pyqtSignal, QSize
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *
import sys


class SettingsUi(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setWindowFlag(Qt.FramelessWindowHint)  # Режим без рамок окна
        self.setStyleSheet('background-color: black')

        self.text_location = ''


        self.initUi()

    def initUi(self):

        self.label_text_settings = QLabel('Настройки')
        self.label_text_settings.setFont(PyQt5.QtGui.QFont('Inter', 20))
        self.label_text_settings.setStyleSheet('color: white')

        self.hbox_settings = QHBoxLayout()
        self.hbox_settings.addWidget(self.label_text_settings)

        self.label_text_description = QLabel('Заполните информацию о вашем местоположении')
        self.label_text_description.setFont(PyQt5.QtGui.QFont('Inter', 16))
        self.label_text_description.setStyleSheet('color: white')

        self.label_text_location = QLabel("Местоположение")
        self.label_text_location.setFont(PyQt5.QtGui.QFont('Inter', 16))
        self.label_text_location.setStyleSheet('color: white')

        self.textbox_location = QLineEdit(self)
        self.textbox_location.move(20,20)
        self.textbox_location.resize(280,40)

        layout_vertical = QVBoxLayout()
        layout_vertical.addWidget(self.label_text_settings)
        layout_vertical.addWidget(self.label_text_description)
        layout_vertical.addWidget(self.label_text_location)
        layout_vertical.addWidget(self.textbox_location)

        grid = QtWidgets.QGridLayout()

        grid.addWidget(self.label_text_settings, 0, 1)
        grid.addWidget(self.label_text_description, 1, 1)
        grid.addWidget(self.label_text_location, 2, 1)
        grid.addWidget(self.textbox_location, 3, 1)

        self.setLayout(layout_vertical)


        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SettingsUi()
    sys.exit(app.exec_())
