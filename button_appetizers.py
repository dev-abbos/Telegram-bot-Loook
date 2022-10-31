from aiogram.types import *
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
            InlineKeyboardButton(text='STRIPS 7 PCS', callback_data='strips7')
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
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_to_menu')
        ]
    ]
)
fries_btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_appetizers'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_cheese_friesbtn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
cheese_friesbtn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_appetizers'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_rustic_friesbtn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
rustic_friesbtn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_appetizers'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_bitesbtn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
bitesbtn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_appetizers'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_friendsbtn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
friendsbtn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_appetizers'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_mushroomsbtn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
mushroomsbtn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_appetizers'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_teriyaki_wingsbtn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
teriyaki_wingsbtn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_appetizers'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_cheese_nuggetsbtn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
cheese_nuggetsbtn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_appetizers'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_strips1btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
strips1btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_appetizers'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_strips3btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
strips3btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_appetizers'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_strips5btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
strips5btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_appetizers'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_strips7btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
strips7btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_appetizers'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_wingsbtn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
wingsbtn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_appetizers'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_hot_wings3btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
hot_wings3btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_appetizers'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_hot_wings5btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
hot_wings5btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_appetizers'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_hot_wings7btn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
hot_wings7btn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_appetizers'),
            InlineKeyboardButton(text='Keyingi ⏩', callback_data='next_chechevit_soupbtn')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)
chechevit_soupbtn = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='➕', callback_data='add'),
            InlineKeyboardButton(text='➖', callback_data='less')
        ],
        [
            InlineKeyboardButton(text='⏪ Orqaga', callback_data='back_appetizers')
        ],
        [
            InlineKeyboardButton(text='⏪ Asosiy menu', callback_data='back_menu')
        ]
    ]
)