from aiogram.types import *
from config import dp

spinnerMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='SPINNER SNACK', callback_data='spinner_snack'),
            InlineKeyboardButton(text='SPINNER SALSA', callback_data='spinner_salsa')
        ],
        [
            InlineKeyboardButton(text='SPINNER TAKO', callback_data='spinner_tako'),
            InlineKeyboardButton(text='SPINNER NO SOUCE', callback_data='spinner_no_souce')
        ],
        [
            InlineKeyboardButton(text='DUET MASTER', callback_data='duet_master'),
            InlineKeyboardButton(text='SMILE BOX', callback_data='smile_box')
        ],
        [
            InlineKeyboardButton(text='SPINNER SUPER CHARGED', callback_data='spinner_super_charged')
        ],
        [
            InlineKeyboardButton(text='🛒 Buyurtmalar', callback_data='orders')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_to_menu')
        ]
    ]
)

