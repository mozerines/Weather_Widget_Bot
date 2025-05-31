from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

weather_kb_buttons = [
    [InlineKeyboardButton(text='Полная информация', callback_data='full_weather')],
    [InlineKeyboardButton(text='В меню', callback_data='menu')]
]

weather_kb = InlineKeyboardMarkup(inline_keyboard=weather_kb_buttons)
