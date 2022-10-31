from aiogram.types import *
from config import dp

chickenMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='CHICKEN 1 PC SPICY', callback_data='chicken_spicy'),
            InlineKeyboardButton(text='CHICKEN 1 PC NORMAL', callback_data='chicken_normal')
        ],
        [
            InlineKeyboardButton(text='SNACK MEAL SPICY', callback_data='snack_meal_spicy'),
            InlineKeyboardButton(text='SNACK MEAL NORMAL', callback_data='snack_meal_normal')
        ],
        [
            InlineKeyboardButton(text='DINNER MEAL SPICY', callback_data='dinner_meal_spicy'),
            InlineKeyboardButton(text='DINNER MEAL NORMAL', callback_data='dinner_meal_normal')
        ],
        [
            InlineKeyboardButton(text='DOUBLE MEAL', callback_data='double_meal'),
            InlineKeyboardButton(text='MIX MEAL NORMAL', callback_data='mix_meal_normal')
        ],
        [
            InlineKeyboardButton(text='12 PCS CHICKEN SET SPICY', callback_data='chicken_set_spicy'),
            InlineKeyboardButton(text='12 PCS CHICKEN SET NORMAL', callback_data='chicken_set_normal')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_to_menu')
        ]
    ]
)

chicken_spicy_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_chickens'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_chicken_normal_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
chicken_normal_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_chickens'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_snack_meal_spicy_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
snack_meal_spicy_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_chickens'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_snack_meal_normal_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
snack_meal_normal_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_chickens'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_dinner_meal_spicy_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
dinner_meal_spicy_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_chickens'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_dinner_meal_normal_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
dinner_meal_normal_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_chickens'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_double_meal_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
double_meal_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_chickens'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_mix_meal_normal_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
mix_meal_normal_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_chickens'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_chicken_set_spicy_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
chicken_set_spicy_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_chickens'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_chicken_set_normal_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
chicken_set_normal_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_chickens')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)