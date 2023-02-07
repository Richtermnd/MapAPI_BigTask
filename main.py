import os
import sys

import requests
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow
from MapUI import Ui_MainWindow
from map_api import *


# (0.005, 0.005) -> (0.005, 0.012)
# Чтобы при нажатие налево картинка смещалась ровно на один экран
requester = MapRequester((55.7, 37.53), "map", (0.005, 0.012))


class UI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.searchbutton.clicked.connect(self.search)
        self.typesmap.currentTextChanged.connect(self.on_combobox_changed)
        self.clear.clicked.connect(self.clear_line)
        self.typesmap.addItems(["Схема", "Спутник", "Гибрид"])
        self.displayImage()

    def on_combobox_changed(self, value):
        # Тут можно просто к аттрибуту map_type обращаться
        if value == "Схема":
            requester.map_type = 'map'
        elif value == "Спутник":
            requester.map_type = 'sat'
        elif value == "Гибрид":
            requester.map_type = 'sat,skl'
        self.displayImage()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp:
            requester.decrease_zoom()
            self.displayImage()
        elif event.key() == Qt.Key_PageDown:
            requester.increase_zoom()
            self.displayImage()
        elif event.key() == Qt.Key_Up:
            requester.move("up")
            self.displayImage()
        elif event.key() == Qt.Key_Down:
            requester.move("down")
            self.displayImage()
        elif event.key() == Qt.Key_Left:
            requester.move("left")
            self.displayImage()
        elif event.key() == Qt.Key_Right:
            requester.move("right")
            self.displayImage()

    # Вывод изображения на экран
    def displayImage(self):
        self.map.setPixmap(requester.get_image())

    # Очистка строки
    def clear_line(self):
        self.searchline.setText("")

    # Поиск
    def search(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UI()
    ex.show()
    sys.exit(app.exec())