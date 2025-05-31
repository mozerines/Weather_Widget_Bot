import datetime

import requests
import time

from keys import API_KEY


def get_city(city: str, lang: str = 'Ru', units: str = 'Metric', key: str = API_KEY) -> dict:
    """
    :param city: City
    :param lang: Language
    :param units: Units
    :param key: API key
    :return: Weather data or error dict
    """
    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&lang={lang}&units={units}&appid={key}'
    response = requests.get(url=url)
    data = response.json()

    # Проверяем код ответа
    if response.status_code != 200:
        print(f"API Error: {data.get('message', 'Unknown error')}")
        return {}

    return data


def get_direction(degrees: float) -> str | None:
    if 0 >= degrees <= 22.5 or 337.5 >= degrees <= 360:
        return 'С'
    elif 22.5 > degrees < 67.5:
        return 'СВ'
    elif 67.5 >= degrees <= 112.5:
        return 'В'
    elif 112.5 > degrees < 167.5:
        return 'ЮВ'
    elif 167.5 >= degrees <= 202.5:
        return 'Ю'
    elif 202.5 > degrees < 247.5:
        return 'ЮЗ'
    elif 247.5 >= degrees <= 292.5:
        return 'З'
    elif 292.5 > degrees < 337.5:
        return 'СЗ'
    else:
        return None

def get_time(timestamp: int):
    unix_time = datetime.datetime.fromtimestamp(timestamp)
    return unix_time.strftime("%Y-%m-%d %H:%M:%S UTC")

def parse_weather_data(api_response: dict) -> dict:
    """Безопасный парсинг данных с проверкой всех полей"""
    if not api_response or api_response.get('cod') != 200:
        return None

    return {
        'temp': round(api_response.get('main', {}).get('temp', 0)),
        'feels_like': round(api_response.get('main', {}).get('feels_like', 0)),
        'humidity': api_response.get('main', {}).get('humidity', 0),
        'pressure': round(api_response.get('main', {}).get('pressure', 0) * 0.750062),
        'wind_speed': api_response.get('wind', {}).get('speed', 0),
        'wind_dir': get_direction(api_response.get('wind', {}).get('deg', 0)),
        'icon': api_response.get('weather', [{}])[0].get('icon', '02d'),
        'description': api_response.get('weather', [{}])[0].get('description', ''),
        'city': api_response.get('name', 'Unknown'),
        'timestamp': api_response.get('dt', int(time.time()))
    }

# weather = str(data['weather'][0]['description']).capitalize()
# icon_name: str = data['weather'][0]['icon']
# print(get_weather())

# img = Image.open(f'icons/{icon_name}@2x.png')
# img.show()
