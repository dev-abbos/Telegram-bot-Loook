from aiogram.types import *

pizzaMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='PIZZA SUPREME', callback_data='pizza_supreme'),
            InlineKeyboardButton(text='PIZZA STEAK', callback_data='pizza_steak')
        ],
        [
            InlineKeyboardButton(text='PIZZA SPICY', callback_data='pizza_spicy'),
            InlineKeyboardButton(text='PIZZA BBQ CHICKEN', callback_data='pizza_bbq_chicken')
        ],
        [
            InlineKeyboardButton(text='PIZZA VEGETARIAN', callback_data='pizza_vegetarian'),
            InlineKeyboardButton(text='PIZZA WHITE CHEESE', callback_data='pizza_white_cheese')
        ],
        [
            InlineKeyboardButton(text='PIZZA HAWAIIAN', callback_data='pizza_hawaiian'),
            InlineKeyboardButton(text='PIZZA PEPPERONI', callback_data='pizza_pepperoni')
        ],
        [
            InlineKeyboardButton(text='PIZZA MARGARITA', callback_data='pizza_margarita'),
            InlineKeyboardButton(text='PIZZA FRANKFURT', callback_data='pizza_frankfurt')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_to_menu')
        ]
    ]
)

pizza_supreme_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_pizza'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_pizza_spicy_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
pizza_spicy_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_pizza'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_pizza_vegetarian_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
pizza_vegetarian_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_pizza'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_pizza_hawaiian_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
pizza_hawaiian_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_pizza'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_pizza_margarita_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
pizza_margarita_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_pizza'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_pizza_steak_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
pizza_steak_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_pizza'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_pizza_bbqchicken_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
pizza_bbqchicken_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_pizza'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_pizza_whitecheese_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
pizza_whitecheese_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_pizza'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_pizza_pepperoni_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
pizza_pepperoni_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_pizza'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_pizza_frankfurt_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
pizza_frankfurt_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_pizza')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)