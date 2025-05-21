import  requests

from keys import API_KEY


def get_city(KEY: str):
    """
    :key == API Key
    :return:
    """

    CITY = input("Введите город: ").lower()
    LANG = input("Введите язык (RU, KZ и т.д.): ").lower()
    UNITS = 'metric'

    url = f'https://api.openweathermap.org/data/2.5/weather?q={CITY}&lang={LANG}&units={UNITS}&appid={KEY}'
    response = requests.get(url=url)
    data = response.json()

    return data

data = get_city(API_KEY)

icon_code = data["weather"][0]["icon"]
icon_url = f"https://openweathermap.org/img/wn/{icon_code}@2x.png"

# Скачиваем иконку
icon_response = requests.get(icon_url)
with open("icons/weather_icon.png", "wb") as f:
    f.write(icon_response.content)