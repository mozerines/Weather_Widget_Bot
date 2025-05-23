from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

lang_kb_buttons = [
    [
        InlineKeyboardButton(text="🇦🇱" ,callback_data='sq'),
        InlineKeyboardButton(text="🇿🇦", callback_data="af"),
        InlineKeyboardButton(text="🇴🇲", callback_data='ar'),
        InlineKeyboardButton(text="🇦🇿", callback_data='az'),
        InlineKeyboardButton(text="eu", callback_data='eu')
     ],
    [
        InlineKeyboardButton(text="🇧🇾", callback_data='be'),
        InlineKeyboardButton(text="🇧🇬", callback_data='bg'),
        InlineKeyboardButton(text="ca", callback_data='ca'),
        InlineKeyboardButton(text="🇨🇳 (simplified)", callback_data='zh-cn'),
        InlineKeyboardButton(text="🇨🇳 (Traditional)", callback_data='zn-tw')
     ],
    [
        InlineKeyboardButton(text="🇭🇷", callback_data='hr'),
        InlineKeyboardButton(text="🇨🇿", callback_data='cz'),
        InlineKeyboardButton(text="🇩🇰", callback_data='da'),
        InlineKeyboardButton(text="🇳🇱", callback_data='nl'),
        InlineKeyboardButton(text="🇺🇸", callback_data='en')
    ],
    [
        InlineKeyboardButton(text="🇫🇮", callback_data='fi'),
        InlineKeyboardButton(text="🇫🇷", callback_data='fr'),
        InlineKeyboardButton(text="gl", callback_data='gl'),
        InlineKeyboardButton(text="🇩🇪", callback_data='de'),
        InlineKeyboardButton(text="🇬🇷", callback_data='el')
    ],
    [
        InlineKeyboardButton(text="🇮🇱", callback_data='he'),
        InlineKeyboardButton(text="🇮🇳", callback_data='hi'),
        InlineKeyboardButton(text="🇭🇺", callback_data='hu'),
        InlineKeyboardButton(text="🇮🇸", callback_data='is'),
        InlineKeyboardButton(text="🇮🇩", callback_data='id')
    ],
    [
        InlineKeyboardButton(text="🇮🇹", callback_data='it'),
        InlineKeyboardButton(text="🇯🇵", callback_data='ja'),
        InlineKeyboardButton(text="🇰🇷", callback_data='kr'),
        InlineKeyboardButton(text="ku", callback_data='ku'),
        InlineKeyboardButton(text="🇱🇻", callback_data='la')
    ],
    [
        InlineKeyboardButton(text="🇱🇹", callback_data='lt'),
        InlineKeyboardButton(text="🇲🇰", callback_data='mk'),
        InlineKeyboardButton(text="🇳🇴", callback_data='no'),
        InlineKeyboardButton(text="🇮🇷", callback_data='fa'),
        InlineKeyboardButton(text="🇵🇱", callback_data='pl')
    ],
    [
        InlineKeyboardButton(text="🇵🇹", callback_data='pt'),
        InlineKeyboardButton(text="🇵🇹-🇧🇷", callback_data='pt_bz'),
        InlineKeyboardButton(text="🇷🇴", callback_data='ro'),
        InlineKeyboardButton(text="🇷🇺", callback_data='ru'),
        InlineKeyboardButton(text="🇷🇸", callback_data='sr')
    ],
    [
        InlineKeyboardButton(text="🇸🇰", callback_data='sk'),
        InlineKeyboardButton(text="🇸🇮", callback_data='sl'),
        InlineKeyboardButton(text="🇪🇸", callback_data='es'),
        InlineKeyboardButton(text="🇸🇪", callback_data='se'),
        InlineKeyboardButton(text="🇹🇭", callback_data='th')
    ],
    [
        InlineKeyboardButton(text="🇹🇷", callback_data='tr'),
        InlineKeyboardButton(text="🇺🇦", callback_data='ua'),
        InlineKeyboardButton(text="🇻🇳", callback_data='vi'),
        InlineKeyboardButton(text="zu", callback_data='zu'),
    ],
    [InlineKeyboardButton(text='Продолжить', callback_data='continue')]
]

lang_kb = InlineKeyboardMarkup(inline_keyboard=lang_kb_buttons)