from pickle import FALSE

from aiogram.types import CallbackQuery, Message

# from owm_api import get_weather
from keyboards.main_kb import lang_kb
from aiogram.filters import Command
from config import *

from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from owm_api import get_city


class WeatherStates(StatesGroup):
    waiting_for_lang = State()
    waiting_for_city = State()


@dp.message(Command('start'))
async def cmd_start(message: Message):
    print('/start получен!')
    await message.answer(text='Выберите язык:', reply_markup=lang_kb)


@dp.callback_query(lambda callback: callback)
async def lang_state(callback: CallbackQuery, state: FSMContext):
    if callback.data != 'continue':
        await state.update_data(lang=callback.data)
        print(callback.data)
        await callback.answer(show_alert=False)

@dp.message()
async def city_state(message: Message, state: FSMContext):
    await state.set_state(WeatherStates.waiting_for_city)
    await state.update_data(city=message.text)
    print(message.text)
    daty = await state.get_data()
    print(daty.get('city'))

@dp.callback_query(lambda callback: callback.data)
async def city_weather(callback: CallbackQuery, state: FSMContext):
    print(callback)
    if callback == 'continue':
        data = await state.get_data()
        print(data)
        city = data.get('city')
        lang = data.get('lang')
        print(get_city(city=city, lang=lang))
