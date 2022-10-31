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
            InlineKeyboardButton(text='🛒 Buyurtmalar', callback_data='orders')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_to_menu')
        ]
    ]
)

