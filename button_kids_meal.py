from aiogram.types import *
from config import dp

kidsMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='KIDS BURGER', callback_data='kids_burger'),
            InlineKeyboardButton(text='KIDS SPINNER', callback_data='kids_spinner')
        ],
        [
            InlineKeyboardButton(text='KIDS MENU STRIPS BOY', callback_data='kids_strips_boy'),
            InlineKeyboardButton(text='KIDS MENU STRIPS GIRL', callback_data='kids_strips_girl')
        ],
        [
            InlineKeyboardButton(text='KIDS MENU SPINNER BOY', callback_data='kids_spinner_boy'),
            InlineKeyboardButton(text='KIDS MENU SPINNER GIRL', callback_data='kids_spinner_girl')
        ],
        [
            InlineKeyboardButton(text='🛒 Buyurtmalar', callback_data='orders')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_to_menu')
        ]
    ]
)

