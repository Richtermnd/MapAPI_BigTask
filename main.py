import os
import sys

import requests
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow
from MapUI import Ui_MainWindow

SCREEN_SIZE = [600, 450]


class UI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.long = 37.53
        self.lat = 55.7
        self.spn_x = 0.005
        self.spn_y = 0.005
        self.map_type = "map"
        self.map_file = None
        self.setupUi(self)
        self.searchbutton.clicked.connect(self.search)
        self.typesmap.currentTextChanged.connect(self.on_combobox_changed)
        self.clear.clicked.connect(self.clear_line)
        self.typesmap.addItems(["Спутник", "Схема", "Гибрид"])

    def on_combobox_changed(self, value):
        if value == "Схема":
            self.map_type = "map"
        elif value == "Спутник":
            self.map_type = "sat"
        elif value == "Гибрид":
            self.map_type = "sat,skl"

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_PageUp:
            self.spn_x /= 2
            self.spn_y /= 2
        elif event.key() == Qt.Key_PageDown:
            self.spn_x *= 2
            self.spn_y *= 2
        elif event.key() == Qt.Key_Up:
            self.lat += self.spn_y
        elif event.key() == Qt.Key_Down:
            self.lat -= self.spn_x
        elif event.key() == Qt.Key_Left:
            self.long -= self.spn_y
        elif event.key() == Qt.Key_Right:
            self.long += self.spn_y

    # Вывод изображения на экран
    def displayImage(self):
        self.pixmap = QPixmap(self.map_file)
        self.map.setPixmap(self.pixmap)
        self.delete_map()

    # Удаление карты
    def delete_map(self):
        """При закрытии формы подчищаем за собой"""
        os.remove(self.map_file)

    # Очистка строки
    def clear_line(self):
        self.searchline.setText("")

    # Поиск
    def search(self):
        self.getImage()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UI()
    ex.show()
    sys.exit(app.exec())