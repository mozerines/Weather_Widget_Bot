import requests, time
from PIL import Image

from keys import API_KEY


def get_city(city: str, lang: str = 'Ru', units: str = 'Metric', key: str = API_KEY, ) -> dict:
    """
    :param city: City
    :param lang: Language
    :param units: Units
    :param key: API key
    :return Weather data
    """

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&lang={lang}&units={units}&appid={key}'
    response = requests.get(url=url)
    weather_data = response.json()
    return weather_data


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



# weather = str(data['weather'][0]['description']).capitalize()
# icon_name: str = data['weather'][0]['icon']
# print(get_weather())

# img = Image.open(f'icons/{icon_name}@2x.png')
# img.show()
