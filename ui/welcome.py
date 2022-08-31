# -*- coding: utf-8 -*-
import sys

import PyQt5.QtGui
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt, QTimer, QTime, pyqtSignal, QSize
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import *


class WelcomeUi(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.text = 'Добро пожаловать!'
        self.setWindowFlag(Qt.FramelessWindowHint)  # Режим без рамок окна
        self.setStyleSheet('background-color: black')

        self.initUi()

    def initUi(self):
        label_welcome = QLabel(f'{self.text}')
        label_welcome.setFont(PyQt5.QtGui.QFont('Inter', 16))
        label_welcome.setStyleSheet('color: white; padding-left: 30px; padding-down: 50px')

        grid = QtWidgets.QGridLayout()  # Создание самой сетки
        "Добавление всех labels в сетку"
        grid.addWidget(label_welcome, 0, 0)

        centerPoint = QDesktopWidget().availableGeometry().center()
        self.setLayout(grid)

        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.center())
        #self.move(self.width(), self.height() // 6)
        self.setWindowTitle('Welcome')
        self.show()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = WelcomeUi()
    sys.exit(app.exec_())
    
