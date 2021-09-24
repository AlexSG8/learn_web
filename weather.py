import requests
import settings
from pprint import pprint


def weather_by_city(city_name, num_of_days=1, response_format='json', lang='ru', token=settings.key):
    weather_url = f'http://api.worldweatheronline.com/premium/v1/weather.ashx'
    params = {
        'key': token,
        'q': city_name,
        'format': response_format,
        'num_of_days': num_of_days,
        'lang': lang
    }
    result = requests.get(weather_url, params=params)
    weather = result.json()
    if 'data' in weather:
        if 'current_condition' in weather['data']:
            try:
                return weather['data']['current_condition'][0]
            except(IndexError, TypeError):
                return False

    return False


if __name__ == '__main__':
    pprint(weather_by_city('Samara,Russia'))
