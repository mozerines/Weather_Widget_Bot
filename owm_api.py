import requests, time
from PIL import Image

from keys import API_KEY


def get_city(city: str, lang: str = 'Ru', units: str = 'Metric', key: str = API_KEY,) -> dict:
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


# def get_weather():
#     data = get_city(API_KEY)
#     print(type(data['cod']))
#     if data['cod'] == 200:
#         print(data)
#
#     elif data['cod'] == '404':
#         print('Город указан неправильно или не существует, проверьте правильность введённых данных.')
#         get_weather()
#
#     elif data['cod'] == '429':
#         print('К сожалению, лимит запросов в минуту или месяц был исчерпан, попробуйте повторить запрос через минуту,'
#               'если ошибка повторится, значит бот недоступен до момента пополнения числа запросов.')
#         get_weather()
#     else:
#         print(f'Код ошибки: {data['cod']}\n'
#               f'Сообщите об этом разработчику @Mozerines')
#         get_weather()
#
#     return data


# get_weather(get_city(API_KEY))

# weather = str(data['weather'][0]['description']).capitalize()
# icon_name: str = data['weather'][0]['icon']
# print(get_weather())

# img = Image.open(f'icons/{icon_name}@2x.png')
# img.show()
