from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton

contactButton = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='📱 Phone number', request_contact=True),
            KeyboardButton(text='📍 Send location', request_location=True)
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

orderMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Menu', callback_data='order')
        ]
    ]
)

chooseMenu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='🍟 APPETIZERS', callback_data='appetizers'),
            InlineKeyboardButton(text='🍔 BURGERS', callback_data='burgers')
        ],
        [
            InlineKeyboardButton(text='🍕 PIZZA', callback_data='pizza'),
            InlineKeyboardButton(text='🌯 SPINNER', callback_data='spinner')
        ],
        [
            InlineKeyboardButton(text='🍗 CHICKEN', callback_data='chicken'),
            InlineKeyboardButton(text='🥗 SALADS AND OTHER', callback_data='salads')
        ],
        [
            InlineKeyboardButton(text='🍰 DESSERTS', callback_data='desserts'),
            InlineKeyboardButton(text='🍹 DRINKS', callback_data='drinks')
        ],
        [
            InlineKeyboardButton(text='🌮 KIDS MEAL', callback_data='kids_meal'),
            InlineKeyboardButton(text='🍟🧃 COMBO', callback_data='combo')
        ],
        [
            InlineKeyboardButton(text='🛒 Buyurtmalar', callback_data='orders')
        ],
        [
            InlineKeyboardButton(text='❌ Bekor qilmoq', callback_data='cancel')
        ]
    ]
)
