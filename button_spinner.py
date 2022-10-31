from aiogram.types import *

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
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_to_menu')
        ]
    ]
)
spinner_snack_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_spinners'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_spinner_tako_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
spinner_tako_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_spinners'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_spinner_salsa_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
spinner_salsa_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_spinners'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_spinner_nosouce_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
spinner_nosouce_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_spinners'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_duet_master_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
duet_master_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_spinners'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_smile_box_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
smile_box_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_spinners'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_spinner_super_charged_btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
spinner_super_charged_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_spinners')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)