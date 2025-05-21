import requests

from keys import API_KEY

def get_city(key: str):
    """
    :key == API Key
    :return:
    """

    city = input("Введите город: ").lower()
    lang = input("Введите язык (RU, KZ и т.д.): ").lower()
    units = 'metric'

    url = f'https://api.openweathermap.org/data/2.5/weather?q={city}&lang={lang}&units={units}&appid={key}'
    response = requests.get(url=url)

    return response.json()


data = get_city(API_KEY)
print(data)

weather = data['weather'][0]
print(weather)