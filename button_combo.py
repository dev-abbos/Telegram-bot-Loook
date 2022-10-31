from aiogram.types import *
from config import dp

comboMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='COMBO', callback_data='combo_')
        ],
        [
            InlineKeyboardButton(text='WICKED COMBO (strips)', callback_data='wicked_combo_strips'),
            InlineKeyboardButton(text='WICKED COMBO (wings)', callback_data='wicked_combo_wings')
        ],
        [
            InlineKeyboardButton(text='FULLY COMBO (normal)', callback_data='fully_combo_normal'),
            InlineKeyboardButton(text='FULLY COMBO (spicy)', callback_data='fully_combo_spicy')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_to_menu')
        ]
    ]
)
combo_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_combo'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_wicked_combo_strips_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
wicked_combo_strips_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_combo'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_wicked_combo_wings_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
wicked_combo_wings_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_combo'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_fully_combo_normal_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
fully_combo_normal_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_combo'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_fully_combo_spicy_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
fully_combo_spicy_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_combo')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)