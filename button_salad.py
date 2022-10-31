from aiogram.types import *
from config import dp

saladMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='COLESLAW SALAD', callback_data='coleslaw_salad'),
            InlineKeyboardButton(text='LOOOK SALAD', callback_data='loook_salad')
        ],
        [
            InlineKeyboardButton(text='VEGGIE FRESH SALAD', callback_data='veggie_fresh_salad'),
            InlineKeyboardButton(text='BREAD PIKELET', callback_data='bread_pikelet')
        ],
        [
            InlineKeyboardButton(text='🛒 Buyurtmalar', callback_data='orders')
        ],
        [
        InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_to_menu')
        ]
    ]
)

