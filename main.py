import os
import sys

import requests
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
        self.clear.clicked.connect(self.clear_line)
        self.typesmap.addItems(["Спутник", "Схема"])
        self.getImage()
        self.displayImage()

    # Получение изображения
    def getImage(self):
        map_params = {
            "ll": f"{self.long},{self.lat}",
            "spn": f"{self.spn_x},{self.spn_y}",
            "l": self.map_type
        }
        map_request = "http://static-maps.yandex.ru/1.x/"
        response = requests.get(map_request, params=map_params)

        if not response:
            print("Ошибка выполнения запроса:")
            print(map_request)
            print("Http статус:", response.status_code, "(", response.reason, ")")
            sys.exit(1)

        # Запишем полученное изображение в файл.
        self.map_file = "map.png"
        with open(self.map_file, "wb") as file:
            file.write(response.content)

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
        self.displayImage()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = UI()
    ex.show()
    sys.exit(app.exec())