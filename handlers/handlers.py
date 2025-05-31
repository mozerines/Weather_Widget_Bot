from aiogram.types import CallbackQuery, Message
from aiogram import F

from handlers.widget import send_weather_widget
from keyboards.developer_kb import developer_kb
from keyboards.main_kb import main_kb
from keyboards.city_kb import city_kb, full_city_kb
from keyboards.lang_kb import lang_kb, lang_callbacks
from keyboards.weather_kb import weather_kb

from aiogram.filters import Command
from config import *

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from owm_api import get_city, get_direction, get_time

import asyncio


class WeatherStates(StatesGroup):
    waiting_for_lang = State()
    waiting_for_city = State()


@dp.message(Command('start'))
async def cmd_start(message: Message, state: FSMContext):
    print('/start получен!')
    await state.set_state(WeatherStates.waiting_for_lang)
    data = await state.get_data()
    if data.get('lang') is None:
        await state.update_data(lang='Ru')
        data = await state.get_data()
    bot_message = await message.answer(text='Главное меню:\n'
                                            f'Язык: {data.get('lang')}\n'
                                            f'Город: {data.get('city')}',
                                       reply_markup=main_kb)
    await state.update_data(bot_message=bot_message.message_id)


@dp.callback_query(lambda callback: callback)
async def callback_handlers(callback: CallbackQuery, state: FSMContext):
    await state.update_data(bot_message=callback.message.message_id)
    if callback.data in lang_callbacks:
        await state.update_data(lang=callback.data)
        print(callback.data)
        print(callback)
        await callback.answer(show_alert=False)
        data = await state.get_data()
        await Weather_widget_bot.edit_message_text(text='Выберите язык\n'
                                                        f'Текущий язык: {str(data.get('lang')).capitalize()}',
                                                   reply_markup=lang_kb,
                                                   chat_id=callback.from_user.id,
                                                   message_id=callback.message.message_id
                                                   )

    if callback.data == 'menu':
        data = await state.get_data()
        if data.get('lang') is None:
            await state.update_data(lang='Ru')
            data = await state.get_data()
        await Weather_widget_bot.edit_message_text(text='Главное меню:\n'
                                                        f'Язык: {data.get('lang')}\n'
                                                        f'Город: {data.get('city')}',
                                                   reply_markup=main_kb,
                                                   chat_id=callback.from_user.id,
                                                   message_id=callback.message.message_id
                                                   )

    if callback.data == 'select_city':
        data = await state.get_data()
        print(data)
        await Weather_widget_bot.edit_message_text(text='Введите название города\n'
                                                        f'Текущий город: {data.get('city')}',
                                                   reply_markup=city_kb,
                                                   chat_id=callback.from_user.id,
                                                   message_id=callback.message.message_id
                                                   )

    if callback.data == 'select_lang':
        data = await state.get_data()
        print(data)
        if data.get('lang') is None:
            await state.update_data(lang='ru')
        await Weather_widget_bot.edit_message_text(text='Выберите язык\n'
                                                        f'Текущий язык: {str(data.get('lang', 'ru')).capitalize()}',
                                                   reply_markup=lang_kb,
                                                   chat_id=callback.from_user.id,
                                                   message_id=callback.message.message_id
                                                   )

    if callback.data == 'city_continue':
        data = await state.get_data()
        print(data)
        city = data.get('city')
        lang = data.get('lang', 'Ru')
        print(city, lang)
        print(get_city(city=city, lang=lang))
        weather_data = get_city(city=city, lang=lang)
        if weather_data['cod'] == 200:
            await callback.message.edit_text(text=f'Город: {weather_data['name']}\n'
                                                  f'Погода: {weather_data['weather'][0]['description']}\n'
                                                  f'Температура: {weather_data['main']['temp']} °С\n'
                                                  f'Ощущается как: {weather_data['main']['feels_like']} °С\n'
                                                  f'Влажность: {weather_data['main']['humidity']} %\n'
                                                  f'Направление и скорость ветра: {get_direction(weather_data['wind']['deg'])},'
                                                  f' {weather_data['wind']['speed']} м/с',
                                             reply_markup=weather_kb)
        elif weather_data['cod'] == 404:
            await callback.answer(text=f'Извините, населённый пункт не существует или введён неправильно, '
                                       f'проверьте правильность введённых данных.',
                                  show_alert=True)
            await callback.message.edit_text(text='Главное меню:\n'
                                                  f'Язык: {data.get('lang')}\n'
                                                  f'Город: {data.get('city')}',
                                             reply_markup=main_kb)
        elif weather_data['cod'] == 429:
            await callback.message.edit_text(
                text=f'Извините, превышен лимит запросов в минуту (60) / месяц (1.000.000),'
                     f'дождитесь обновления числа запросов!',
                reply_markup=weather_kb)
        else:
            await callback.answer(text=f'Возникла ошибка, пожалуйста, сообщите об этом разработчику,'
                                       f' указав код ошибки: {weather_data['cod']}')
            await callback.message.edit_text(text='Главное меню:\n'
                                                  f'Язык: {data.get('lang')}\n'
                                                  f'Город: {data.get('city')}',
                                             reply_markup=main_kb)

    if callback.data == 'full_weather':
        data = await state.get_data()
        city = data.get('city')
        lang = data.get('lang', 'Ru')
        weather_data = get_city(city=city, lang=lang)
        await callback.message.edit_text(
            text=f'Координаты: {weather_data['coord']['lon']}, {weather_data['coord']['lat']}\n\n'
                 f'<b>Погода</b>:\n'
                 f'{weather_data['weather'][0]['description']}\n\n'
                 f'Температура: {weather_data['main']['temp']}°C\n'
                 f'Ощущается как: {weather_data['main']['feels_like']} °C\n'
                 f'Минимальная температура: {weather_data['main']['temp_min']} °C\n'
                 f'Максимальная температура: {weather_data['main']['temp_max']} °C\n'
                 f'Давление: {weather_data['main']['pressure']} hPa\n'
                 f'Влажность: {weather_data['main']['humidity']}%\n'
                 f'Давление на уровне моря: {weather_data['main']['sea_level']} hPa\n'
                 f'Давление на уровне земли: {weather_data['main']['grnd_level']} hPa\n'
                 f'Видимость: {weather_data['visibility']} м\n\n'
                 f'<b>Ветер</b>:\n'
                 f'Скорость ветра: {weather_data['wind']['speed']} м/с\n'
                 f'Направление ветра: {get_direction(weather_data['wind']['deg'])}\n'
                 f'Облачность: {weather_data['clouds']['all']}%\n'
                 f'Время расчёта погоды: {get_time(weather_data['dt'])}\n'
                 f'Код страны: {weather_data['sys']['country']}\n'
                 f'Рассвет: {get_time(weather_data['sys']['sunrise'])}\n'
                 f'Закат: {get_time(weather_data['sys']['sunset'])}\n'
                 f'Временная зона: {weather_data['timezone']}\n'
                 f'ID города: {weather_data['id']}\n'
                 f'Название города: {weather_data['name']}',
            reply_markup=full_city_kb,
            parse_mode='HTML')
    if callback.data == 'developer':
        await callback.message.edit_text(text=f'Разработчик данного бота: Mozerines (Владислав Муругов)\n'
                                              f'Используемый сервис: Open Weather Map\n\n'
                                              f'<b>Социальные сети разработчика</b>:\n'
                                              f'Telegram: @Mozerines\n'
                                              f'ВКонтакте: <a href="https://vk.com/mozerines">Владислав Муругов</a>',
                                         parse_mode='HTML',
                                         reply_markup=developer_kb)

    if callback.data == 'refresh_widget':
        async def refresh_widget(callback: CallbackQuery, state: FSMContext):
            """Обновление виджета"""
            data = await state.get_data()
            await send_weather_widget(callback.message.chat.id, data['city'], Weather_widget_bot)
            await callback.answer("Виджет обновлен!")

@dp.message(Command('widget'))
async def start_widget(message: Message, state: FSMContext):
    try:
        # Можно запросить город через FSM
        data = await state.get_data()  # Замените на реальный ввод
        await send_weather_widget(message.chat.id, data.get('city'), Weather_widget_bot)
    except Exception as e:
        print(f"Ошибка в start_widget: {e}")
        await message.answer("⚠️ Не удалось запустить виджет")


@dp.message()
async def city_state(message: Message, state: FSMContext):
    await message.delete()

    city = message.text.strip()
    await state.update_data(city=city)
    data = await state.get_data()

    print(data.get('city'))
    await message.bot.edit_message_text(chat_id=message.chat.id,
                                        message_id=data['bot_message'],
                                        text=f'Введите название города\n'
                                             f'Текущий город: {city}',
                                        reply_markup=city_kb)



