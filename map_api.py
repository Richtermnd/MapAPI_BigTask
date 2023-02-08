import requests
from PyQt5.QtGui import QPixmap


def convert_coords(coords):
    """ Convert coords to Yandex API forma"""
    lat, lon = coords
    return f'{lon},{lat}'


class MapRequester:

    def __init__(self, ll: tuple,  map_type: str, spn: tuple):
        """
        :param ll: (lat, lon)
        :param map_type: 'map', 'sat' or 'sat,skl'
        :param spn: (lat, lon)
        """
        self.lat = ll[0]
        self.lon = ll[1]
        self.spn_lat = spn[0]
        self.spn_lon = spn[1]
        self.map_type = map_type

    def search(self, address):
        request = "http://geocode-maps.yandex.ru/1.x/"
        params = {
            "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
            "geocode": address,
            "format": "json"}

        response = requests.get(request, params=params)

        if not response:
            print(response.content)
            return

        obj = response.json()["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        lon, lat = [float(x) for x in obj["Point"]["pos"].split()]
        self.lat = lat
        self.lon = lon

    def increase_zoom(self):
        self.spn_lat *= 1.5
        self.spn_lon *= 1.5

    def decrease_zoom(self):
        self.spn_lat /= 1.5
        self.spn_lon /= 1.5

    def move(self, direction):
        match direction:
            case 'left':
                self.lon -= self.spn_lon
            case 'right':
                self.lon += self.spn_lon
            case 'down':
                self.lat -= self.spn_lat
            case 'up':
                self.lat += self.spn_lat

    def params(self):
        params = {'size': '650,450',
                  'll': convert_coords((self.lat, self.lon)),
                  'spn': convert_coords((self.spn_lat, self.spn_lon)),
                  'l': self.map_type}
        return params

    def get_image(self):
        """
        Возвращает QPixmap
        При ошибке возвращает печатает request и возвращает None
        """
        map_api_server = "http://static-maps.yandex.ru/1.x/"
        response = requests.get(map_api_server, params=self.params())
        if not response:
            print(response.content)
            return
        pixmap = QPixmap()
        pixmap.loadFromData(response.content)
        return pixmap
