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
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_to_menu')
        ]
    ]
)
mineralka_05bg_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_drinks'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_mineralka_05g_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
mineralka_05g_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_drinks'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_mineralka_1bg_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
mineralka_1bg_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_drinks'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_mineralka_1g_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
mineralka_1g_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_drinks'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_mineralka_15bg_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
mineralka_15bg_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_drinks'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_mineralka_15g_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
mineralka_15g_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_drinks'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_cola_400_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
cola_400_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_drinks'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_cola_05_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
cola_05_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_drinks'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_cola_1_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
cola_1_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_drinks'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_cola_15_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
cola_15_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_drinks'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_fanta_400_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
fanta_400_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_drinks'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_fanta_05_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
fanta_05_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_drinks'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_fanta_1_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
fanta_1_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_drinks'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_fanta_15_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
fanta_15_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_drinks'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_sprite_400_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
sprite_400_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_drinks'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_sprite_05_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
sprite_05_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_drinks'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_sprite_1_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
sprite_1_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_drinks'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_sprite_15_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
sprite_15_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_drinks'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_ice_tea_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
ice_tea_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_drinks'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_sok_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
sok_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_drinks'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_sok_granat_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
sok_granat_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_drinks'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_sok_apelsin_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
sok_apelsin_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_drinks')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)





