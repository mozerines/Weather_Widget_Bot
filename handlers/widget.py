import time
from typing import Any

from aiogram import Bot
from aiogram.types import InputMediaPhoto, BufferedInputFile

from keyboards.widget_kb import get_widget_keyboard
from handlers.storage_df import get_stored_message_id, save_message_id
from owm_api import get_city, get_direction, parse_weather_data
from services.widget_generator import WeatherWidgetGenerator


def get_weather_for_widget(city: str, lang: str = 'ru') -> dict[str, int | str | None] | None:
    """Безопасный парсинг данных API с проверкой всех полей"""
    try:
        data = get_city(city, lang)

        # Проверяем код ответа и наличие обязательных полей
        if not data or 'cod' in data and data['cod'] != 200:
            error_msg = data.get('message', 'Unknown API error')
            print(f"API Error: {error_msg}")
            return None

        # Безопасное извлечение данных
        weather = {
            'temp': round(data.get('main', {}).get('temp', 0)),
            'wind_speed': data.get('wind', {}).get('speed', 0),
            'wind_dir': get_direction(data.get('wind', {}).get('deg', 0)),
            'humidity': data.get('main', {}).get('humidity', 0),
            'pressure': round(data.get('main', {}).get('pressure', 0) * 0.750062),
            'icon': data.get('weather', [{}])[0].get('icon', '02d'),  # Дефолтная иконка
            'city': data.get('name', city),  # Используем переданный город, если name отсутствует
            'timestamp': data.get('dt', int(time.time()))
        }

        # Дополнительная проверка ключевых полей
        if not weather['icon'] or not weather['city']:
            raise ValueError("Invalid weather data structure")

        return weather

    except Exception as e:
        print(f"Weather parsing error: {e}")
        return None


async def send_weather_widget(chat_id: int, city: str, bot: Bot):
    try:
        # Получаем и парсим данные
        raw_data = get_city(city)
        weather_data = parse_weather_data(raw_data)

        if not weather_data:
            await bot.send_message(chat_id, "❌ Не удалось получить данные")
            return

        # Генерация и отправка
        generator = WeatherWidgetGenerator()
        widget = generator.generate_widget(weather_data)

        await bot.send_photo(
            chat_id=chat_id,
            photo=BufferedInputFile(widget.getvalue(), "weather.png"),
            caption=f"Погода в {weather_data['city']}",
            reply_markup=get_widget_keyboard()
        )

    except Exception as e:
        print(f"Failed to send widget: {e}")
        await bot.send_message(chat_id, "⚠️ Ошибка при создании виджета")