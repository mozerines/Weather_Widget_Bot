from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

main_kb_buttons = [
    [InlineKeyboardButton(text='Смена языка вывода погоды', callback_data='select_lang')],
    [InlineKeyboardButton(text='Посмотреть погоду в городе', callback_data='select_city')],
    [InlineKeyboardButton(text='Разработчик', callback_data='developer')]
]

main_kb = InlineKeyboardMarkup(inline_keyboard=main_kb_buttons)
