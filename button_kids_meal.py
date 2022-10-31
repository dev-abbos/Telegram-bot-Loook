from aiogram.types import *

kidsMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='KIDS BURGER', callback_data='kids_burger'),
            InlineKeyboardButton(text='KIDS SPINNER', callback_data='kids_spinner')
        ],
        [
            InlineKeyboardButton(text='KIDS MENU STRIPS BOY', callback_data='kids_strips_boy'),
            InlineKeyboardButton(text='KIDS MENU STRIPS GIRL', callback_data='kids_strips_girl')
        ],
        [
            InlineKeyboardButton(text='KIDS MENU SPINNER BOY', callback_data='kids_spinner_boy'),
            InlineKeyboardButton(text='KIDS MENU SPINNER GIRL', callback_data='kids_spinner_girl')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_to_menu')
        ]
    ]
)
kids_burger_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_kids_meal'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_kids_spinner_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
kids_spinner_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_kids_meal'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_kids_menu_strips_boy_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
kids_menu_strips_boy_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_kids_meal'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_kids_menu_strips_girl_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
kids_menu_strips_girl_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_kids_meal'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_kids_menu_spinner_boy_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
kids_menu_spinner_boy_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_kids_meal'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_kids_menu_spinner_girl_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
kids_menu_spinner_girl_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_kids_meal')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)