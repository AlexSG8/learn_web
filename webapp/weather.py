from flask import current_app
import requests


def weather_by_city(city_name, num_of_days=1,
                    lang='ru'):

    params = {
        'key': current_app.config['WEATHER_API_KEY'],
        'q': city_name,
        'format': 'json',
        'num_of_days': num_of_days,
        'lang': lang
    }
    try:
        result = requests.get(current_app.config['WEATHER_URL'], params=params)
        result.raise_for_status()
        weather = result.json()
        if 'data' in weather:
            if 'current_condition' in weather['data']:
                try:
                    return weather['data']['current_condition'][0]
                except(IndexError, TypeError):
                    return False
    except(requests.RequestException, ValueError):
        return False
    return False
