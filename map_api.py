import requests
from PyQt5.QtGui import QPixmap
import math


def distance(p1, p2):
    degree_to_meters_factor = 111 * 1000
    a_lat, a_lon = p1
    b_lat, b_lon = p2

    radians_latitude = math.radians((a_lat + b_lat) / 2.)
    lat_lon_factor = math.cos(radians_latitude)

    dx = abs(a_lon - b_lon) * degree_to_meters_factor * lat_lon_factor
    dy = abs(a_lat - b_lat) * degree_to_meters_factor

    return math.sqrt(dx * dx + dy * dy)


def convert_coords(coords):
    """ Convert coords to Yandex API format"""
    lat, lon = coords
    return f'{lon},{lat}'


class MapRequester:

    def __init__(self, ll: tuple,  map_type: str, spn: tuple):
        """
        :param ll: (lat, lon)
        :param map_type: 'map', 'sat' or 'sat,skl'
        :param spn: (lat, lon)
        """
        self.lat, self.lon = ll
        self.spn_lat, self.spn_lon = spn
        self.map_type = map_type
        self.mark_lat, self.mark_lon = 0, 0
        self.is_mark = False
        self.geo_obj = None
        self.org_obj = None

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
        self.geo_obj = obj
        self.lat, self.lon = lat, lon
        self.mark_lat, self.mark_lon = lat, lon
        self.is_mark = True

    def get_address(self, postal_code=False):
        address = self.geo_obj["metaDataProperty"]["GeocoderMetaData"]["Address"]["formatted"]
        if postal_code:
            if "postal_code" in self.geo_obj["metaDataProperty"]["GeocoderMetaData"]["Address"].keys():
                address += ' ' + self.geo_obj["metaDataProperty"]["GeocoderMetaData"]["Address"]["postal_code"]
            else:
                address += " Нет почтового индекса"
        return address

    def get_org(self):
        """
        НЕ РАБОТАЕТ
        Потом реворкну
        """
        request = "https://search-maps.yandex.ru/v1/"
        api_key = 'dda3ddba-c9ea-4ead-9010-f43fbc15c6e3'
        params = {
            "apikey": api_key,
            'text': self.get_address(),
            "lang": "ru_RU",
            "type": "biz"
        }
        response = requests.get(request, params=params)
        if not response:
            print(response.content)
            return
        json_response = response.json()
        lon, lat = json_response['features'][0]["geometry"]["coordinates"]
        if distance((self.lat, self.lon), (lat, lon)) <= 50:
            return json_response['features'][0]["properties"]["CompanyMetaData"]["name"]
        else:
            return ''

    def reset(self):
        self.is_mark = False
        self.geo_obj = None

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
        if self.is_mark:
            params['pt'] = f'{convert_coords((self.mark_lat, self.mark_lon))},pm2bll'
        return params

    def set_coords(self, lat, lon):
        self.lat, self.lon = lat, lon
        self.is_mark = True

    def set_mark_coords(self, lat, lon):
        self.mark_lat, self.mark_lon = lat, lon

    def get_image(self):
        """
        Возвращает QPixmap
        При ошибке печатает request и возвращает пустой Qpixmap
        """
        map_api_server = "http://static-maps.yandex.ru/1.x/"
        response = requests.get(map_api_server, params=self.params())
        if not response:
            print(response.content)
            return QPixmap()
        pixmap = QPixmap()
        pixmap.loadFromData(response.content)
        return pixmap


requester = MapRequester((51.777781, 55.108994), "map", (0.005, 0.012))
requester.search('Проспект Победы 13к3')
print(requester.get_org())
