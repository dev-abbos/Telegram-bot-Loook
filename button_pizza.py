from aiogram.types import *
from config import dp

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
            InlineKeyboardButton(text='🛒 Buyurtmalar', callback_data='orders')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_to_menu')
        ]
    ]
)

