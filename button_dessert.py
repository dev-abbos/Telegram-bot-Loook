from aiogram.types import *
from config import dp

dessertMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='RED WAVE', callback_data='red_wave'),
            InlineKeyboardButton(text='LEMON CAKE', callback_data='lemon_cake')
        ],
        [
            InlineKeyboardButton(text='KIWIX', callback_data='kiwix'),
            InlineKeyboardButton(text='CHOCOTASTIC', callback_data='chocotastic')
        ],
        [
            InlineKeyboardButton(text='TELLO', callback_data='tello'),
            InlineKeyboardButton(text='SUGAR CHIP', callback_data='sugar_chip')
        ],
        [
            InlineKeyboardButton(text='CHOCOLATE SOUFFLE', callback_data='chocolate_souffle'),
        ],
        [
            InlineKeyboardButton(text='🛒 Buyurtmalar', callback_data='orders')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_to_menu')
        ]
    ]
)

