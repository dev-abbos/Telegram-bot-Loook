from aiogram.types import *
from config import dp

chickenMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='CHICKEN 1 PC SPICY', callback_data='chicken1_spicy'),
            InlineKeyboardButton(text='CHICKEN 1 PC NORMAL', callback_data='chicken1_normal')
        ],
        [
            InlineKeyboardButton(text='SNACK MEAL SPICY', callback_data='snack_meal_spicy'),
            InlineKeyboardButton(text='SNACK MEAL NORMAL', callback_data='snack_meal_normal')
        ],
        [
            InlineKeyboardButton(text='DINNER MEAL NORMAL', callback_data='dinner_meal_normal'),
            InlineKeyboardButton(text='DINNER MEAL SPICY', callback_data='dinner_meal_spicy')
        ],
        [
            InlineKeyboardButton(text='MIX MEAL NORMAL', callback_data='mix_meal_normal'),
            InlineKeyboardButton(text='DOUBLE MEAL', callback_data='double_meal')
        ],
        [
            InlineKeyboardButton(text='12 PCS CHICKEN SET NORMAL', callback_data='chicken12_set_normal'),
            InlineKeyboardButton(text='12 PCS CHICKEN SET SPICY', callback_data='chicken12_set_spicy')
        ],
        [
            InlineKeyboardButton(text='🛒 Buyurtmalar', callback_data='orders')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_to_menu')
        ]
    ]
)


