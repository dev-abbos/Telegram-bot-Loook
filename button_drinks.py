from aiogram.types import *
from config import dp

drinksMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='MINERALKA 0.5L BEZGAZ', callback_data='mineralka_0_5bg'),
            InlineKeyboardButton(text='FANTA 0.5L', callback_data='fanta_0_5')
        ],
        [
            InlineKeyboardButton(text='MINERALKA 0.5L GAZ', callback_data='mineralka_0_5g'),
            InlineKeyboardButton(text='FANTA 1L', callback_data='fanta_1')
        ],
        [
            InlineKeyboardButton(text='MINERALKA 1L BEZGAZ', callback_data='mineralka_1bg'),
            InlineKeyboardButton(text='FANTA 1.5L', callback_data='fanta_1_5')
        ],
        [
            InlineKeyboardButton(text='MINERALKA 1L GAZ', callback_data='mineralka_1g'),
            InlineKeyboardButton(text='SPRITE 400ML', callback_data='sprite_400')
        ],
        [
            InlineKeyboardButton(text='MINERALKA 1.5L BEZGAZ', callback_data='mineralka_1_5bg'),
            InlineKeyboardButton(text='SPRITE 0.5L', callback_data='sprite_0_5')
        ],
        [
            InlineKeyboardButton(text='MINERALKA 1.5L GAZ', callback_data='mineralka_1_5g'),
            InlineKeyboardButton(text='SPRITE 1L', callback_data='sprite_1')
        ],
        [
            InlineKeyboardButton(text='COCA COLA 400ML', callback_data='coca_cola_400'),
            InlineKeyboardButton(text='SPRITE 1.5L', callback_data='sprite_1_5')
        ],
        [
            InlineKeyboardButton(text='COCA COLA 0.5L', callback_data='coca_cola_0_5'),
            InlineKeyboardButton(text='ICE TEA', callback_data='ice_tea')
        ],
        [
            InlineKeyboardButton(text='COCA COLA 1L', callback_data='coca_cola_1'),
            InlineKeyboardButton(text='SOK 1L', callback_data='sok_1')
        ],
        [
            InlineKeyboardButton(text='COCA COLA 1.5L', callback_data='coca_cola_1_5'),
            InlineKeyboardButton(text='SOK 1L (GRANAT)', callback_data='sok_1_gr')
        ],
        [
            InlineKeyboardButton(text='FANTA 400ML', callback_data='fanta_400'),
            InlineKeyboardButton(text='SOK 1L (APELSIN)', callback_data='sok_1_ap')
        ],
        [
            InlineKeyboardButton(text='🛒 Buyurtmalar', callback_data='orders')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_to_menu')
        ]
    ]
)




























