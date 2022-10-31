from aiogram.types import *
from config import dp

burgersMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='CLASSIC', callback_data='classic'),
            InlineKeyboardButton(text='JUNIOR BURGER', callback_data='junior_burger')
        ],
        [
            InlineKeyboardButton(text='LONGER', callback_data='longer'),
            InlineKeyboardButton(text='HAMBURGER', callback_data='hamburger')
        ],
        [
            InlineKeyboardButton(text='BIGGER', callback_data='bigger'),
            InlineKeyboardButton(text='CHEESE BURGER', callback_data='cheese_burger')
        ],
        [
            InlineKeyboardButton(text='CHILI LONGER', callback_data='chili_longer'),
            InlineKeyboardButton(text='BARBECUE BURGER', callback_data='barbecue_burger')

        ],
        [
            InlineKeyboardButton(text='BEEF LONGER', callback_data='beef_longer'),
            InlineKeyboardButton(text='CHICKY BURGER', callback_data='chicky_burger')
        ],
        [
            InlineKeyboardButton(text='CHEESY BURGER', callback_data='cheesy_burger'),
            InlineKeyboardButton(text='ROAST BURGER', callback_data='roast_burger')
        ],
        [
            InlineKeyboardButton(text='DOUBLE CHEESE BURGER', callback_data='double_cheese_burger')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_to_menu')
        ]
    ]
)
classic_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_burgers'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_longer_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
longer_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_burgers'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_bigger_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
bigger_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_burgers'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_chili_longer_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
chili_longer_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_burgers'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_beef_longer_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
beef_longer_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_burgers'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_cheesy_burger_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
cheesy_burger_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_burgers'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_junior_burger_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
junior_burger_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_burgers'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_hamburger_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
hamburger_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_burgers'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_cheese_burger_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
cheese_burger_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_burgers'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_barbecue_burger_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
barbecue_burger_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_burgers'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_chicky_burger_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
chicky_burger_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_burgers'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_roast_burger_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
roast_burger_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_burgers'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_double_cheese_burger_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
double_cheese_burger_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_burgers')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)