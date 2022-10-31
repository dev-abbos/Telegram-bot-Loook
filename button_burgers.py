from aiogram.types import *
from config import dp

burgersMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='CLASSIC', callback_data='classic'),
            InlineKeyboardButton(text='JUNIOR BURGER', callback_data='junior_burger')
        ],
        [
            InlineKeyboardButton(text='LONGER', callback_data='longer'),
            InlineKeyboardButton(text='HAMBURGER', callback_data='hamburger')
        ],
        [
            InlineKeyboardButton(text='BIGGER', callback_data='bigger'),
            InlineKeyboardButton(text='CHEESE BURGER', callback_data='cheese_burger')
        ],
        [
            InlineKeyboardButton(text='CHILI LONGER', callback_data='chili_longer'),
            InlineKeyboardButton(text='BARBECUE BURGER', callback_data='barbecue_burger')

        ],
        [
            InlineKeyboardButton(text='BEEF LONGER', callback_data='beef_longer'),
            InlineKeyboardButton(text='CHICKY BURGER', callback_data='chicky_burger')
        ],
        [
            InlineKeyboardButton(text='CHEESY BURGER', callback_data='cheesy_burger'),
            InlineKeyboardButton(text='ROAST BURGER', callback_data='roast_burger')
        ],
        [
            InlineKeyboardButton(text='DOUBLE CHEESE LONGER', callback_data='double_cheese_longer')
        ],
        [
            InlineKeyboardButton(text='🛒 Buyurtmalar', callback_data='orders')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_to_menu')
        ]
    ]
)

