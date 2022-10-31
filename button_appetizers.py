from aiogram.types import *
from config import dp
appetizersMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='FRIES', callback_data='fries'),
            InlineKeyboardButton(text='STRIPS 1 PC', callback_data='strips1')
        ],
        [
            InlineKeyboardButton(text='CHEESE FRIES', callback_data='cheese_fries'),
            InlineKeyboardButton(text='STRIPS 3 PCS', callback_data='strips3')
        ],
        [
            InlineKeyboardButton(text='RUSTIC FRIES', callback_data='rustic_fries'),
            InlineKeyboardButton(text='STRIPS 5 PCS', callback_data='strips5')

        ],
        [
            InlineKeyboardButton(text='BITES', callback_data='bites'),
            InlineKeyboardButton(text='STRIPS 7 PCS', callback_data='strips7'),


        ],
        [
            InlineKeyboardButton(text='FRIENDS', callback_data='friends'),
            InlineKeyboardButton(text='WINGS 1 PC', callback_data='wings1')

        ],
        [
            InlineKeyboardButton(text='MUSHROOMS', callback_data='mushrooms'),
            InlineKeyboardButton(text='HOT WINGS 3 PCS', callback_data='hot_wings3')

        ],
        [
            InlineKeyboardButton(text='TERIYAKI WINGS 3 PCS', callback_data='teriyaki_wings3'),
            InlineKeyboardButton(text='HOT WINGS 5 PCS', callback_data='hot_wings5')
        ],
        [
            InlineKeyboardButton(text='CHEESE NUGGETS 5 PCS', callback_data='cheese_nuggets'),
            InlineKeyboardButton(text='HOT WINGS 7 PCS', callback_data='hot_wings7')
        ],
        [
            InlineKeyboardButton(text='CHECHEVIT SOUP', callback_data='chechevit_soup')
        ],
        [
            InlineKeyboardButton(text='🛒 Buyurtmalar', callback_data='orders')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_to_menu')
        ]
    ]
)

fries_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Harid qilmoq', callback_data='purchase')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next')
        ]
    ]
)
