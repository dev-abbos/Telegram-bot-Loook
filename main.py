from aiogram import executor
from button_menu import chooseMenu, orderMenu, contactButton, infobtn
from button_appetizers import *
from button_kids_meal import *
from button_salad import *
from button_spinner import *
from button_burgers import *
from button_chicken import *
from button_combo import *
from button_drinks import *
from button_pizza import *
from button_dessert import *
from config import dp
import logging

logging.basicConfig(level=logging.INFO)

# START
@dp.message_handler(commands='start')
async def start(msg: Message):
    img = open('images/loook.jpg', 'rb')
    txt = '<b>Assalom aleykum!</b>\n<b><i>"LOOOK"</i></b>' \
          'buyurtma botiga hush kelibsiz!\n'
    await msg.answer_photo(img, caption=txt, parse_mode='html', reply_markup=orderMenu)

# INFO
@dp.message_handler(commands='info')
async def url(msg: Message):
    await msg.answer('Biz haqimizda batafsil ma\'lumot:', reply_markup=infobtn)


# MENU
@dp.callback_query_handler(text='order')
async def to_menu(call: CallbackQuery):
    img = open('images/loook menu.png', 'rb')
    await call.message.answer_photo(img, reply_markup=chooseMenu)
    await call.message.delete()
    await call.answer(cache_time=30)

# BACK TO MENU
@dp.callback_query_handler(text='back_to_menu')
async def to_menu(call: CallbackQuery):
    img = open('images/loook menu.png', 'rb')
    await call.message.answer_photo(img, reply_markup=chooseMenu)
    await call.message.delete()
    await call.answer(cache_time=30)

# BACK TO MENU from subsubmenu
@dp.callback_query_handler(text='back_menu')
async def back(call: CallbackQuery):
    img = open('images/loook menu.png', 'rb')
    await call.message.answer_photo(img, reply_markup=chooseMenu)
    await call.message.delete()
    await call.answer(cache_time=30)

# BACK TO APPETIZERS MENU
@dp.callback_query_handler(text='back_appetizers')
async def back(call: CallbackQuery):
    await call.message.answer('<b>APPETIZERS MENU</b>', parse_mode='html', reply_markup=appetizersMenu)
    await call.message.delete()
    await call.answer(cache_time=30)

# BACK TO BURGERS MENU
@dp.callback_query_handler(text='back_burgers')
async def back(call: CallbackQuery):
    await call.message.answer('<b>BURGERS MENU</b>', parse_mode='html', reply_markup=burgersMenu)
    await call.message.delete()
    await call.answer(cache_time=30)

# BACK TO PIZZA MENU
@dp.callback_query_handler(text='back_pizza')
async def back(call: CallbackQuery):
    await call.message.answer('<b>PIZZA MENU</b>', parse_mode='html', reply_markup=pizzaMenu)
    await call.message.delete()
    await call.answer(cache_time=30)

# BACK TO SPINNERS MENU
@dp.callback_query_handler(text='back_spinners')
async def back(call: CallbackQuery):
    await call.message.answer('<b>SPINNER MENU</b>', parse_mode='html', reply_markup=spinnerMenu)
    await call.message.delete()
    await call.answer(cache_time=30)

# BACK TO CHICKENS MENU
@dp.callback_query_handler(text='back_chickens')
async def back(call: CallbackQuery):
    await call.message.answer('<b>CHICKENS MENU</b>', parse_mode='html', reply_markup=chickenMenu)
    await call.message.delete()
    await call.answer(cache_time=30)

# BACK TO SALADS AND OTHER MENU
@dp.callback_query_handler(text='back_salads')
async def back(call: CallbackQuery):
    await call.message.answer('<b>SALADS AND OTHER MENU</b>', parse_mode='html', reply_markup=saladMenu)
    await call.message.delete()
    await call.answer(cache_time=30)

# BACK TO DESSERTS MENU
@dp.callback_query_handler(text='back_desserts')
async def back(call: CallbackQuery):
    await call.message.answer('<b>DESSERTS MENU</b>', parse_mode='html', reply_markup=dessertMenu)
    await call.message.delete()
    await call.answer(cache_time=30)

# BACK TO DRINKS MENU
@dp.callback_query_handler(text='back_drinks')
async def back(call: CallbackQuery):
    await call.message.answer('<b>DRINKS MENU</b>', parse_mode='html', reply_markup=drinksMenu)
    await call.message.delete()
    await call.answer(cache_time=30)

# BACK TO KIDS MEAL MENU
@dp.callback_query_handler(text='back_kids_meal')
async def back(call: CallbackQuery):
    await call.message.answer('<b>KIDS MEAL MENU</b>', parse_mode='html', reply_markup=kidsMenu)
    await call.message.delete()
    await call.answer(cache_time=30)

# BACK TO COMBO MENU
@dp.callback_query_handler(text='back_combo')
async def back(call: CallbackQuery):
    await call.message.answer('<b>COMBO MENU</b>', parse_mode='html', reply_markup=comboMenu)
    await call.message.delete()
    await call.answer(cache_time=30)

# CANCEL
@dp.callback_query_handler(text='cancel')
async def cancel(call: CallbackQuery):
    img = open('images/loook.jpg', 'rb')
    txt = '<b>Assalom aleykum!</b>\n<b><i>"LOOOK"</i></b>' \
          'buyurtma botiga hush kelibsiz!\n'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=orderMenu)
    await call.message.delete()
    await call.answer(cache_time=30)

# ADD (MAKE PURCHASE)
@dp.callback_query_handler(text='add')
async def back(call: CallbackQuery):
    await call.answer('Qo\'shildi!', show_alert=True)
    await call.answer(cache_time=30)

# LESS (CANCEL PURCHASE)
@dp.callback_query_handler(text='less')
async def back(call: CallbackQuery):
    await call.answer('Bekor qilindi!', show_alert=True)
    await call.answer(cache_time=30)

# Buyurtmani tasdiqlash (CONFIRM PURCHASE)
@dp.callback_query_handler(text='confirm_purchase')
async def back(call: CallbackQuery):
    await call.message.answer('<b>Ma\'lumotingizni jo\'nating!</b>', parse_mode='html', reply_markup=contactButton)
    await call.message.delete()
    await call.answer(cache_time=30)


# APPETIZERS
@dp.callback_query_handler(text='appetizers')
async def appetizers(call: CallbackQuery):
    await call.message.answer('<b>APPETIZERS MENU</b>', parse_mode='html', reply_markup=appetizersMenu)
    await call.message.delete()
    await call.answer(cache_time=30)

# APPETIZERS => FRIES
@dp.callback_query_handler(text='fries')
async def fries(call: CallbackQuery):
    img = open('images/APPETIZERS/fries.jpg', 'rb')
    txt = '<b>FRIES 11.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=fries_btn)
    await call.message.delete()

# APPETIZERS => NEXT CHEESE FRIES
@dp.callback_query_handler(text='next_cheese_friesbtn')
async def back(call: CallbackQuery):
    img = open('images/APPETIZERS/cheese fries.png', 'rb')
    txt = '<b>CHEESE FRIES 13.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=cheese_friesbtn)
    await call.message.delete()

# APPETIZERS => CHEESE FRIES
@dp.callback_query_handler(text='cheese_fries')
async def cheese_fries(call: CallbackQuery):
    img = open('images/APPETIZERS/cheese fries.png', 'rb')
    txt = '<b>CHEESE FRIES 13.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=cheese_friesbtn)
    await call.message.delete()

# APPETIZERS => NEXT RUSTIC FRIES
@dp.callback_query_handler(text='next_rustic_friesbtn')
async def back(call: CallbackQuery):
    img = open('images/APPETIZERS/rustic fries.png', 'rb')
    txt = '<b>RUSTIC FRIES 14.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=rustic_friesbtn)
    await call.message.delete()

# APPETIZERS => RUSTIC FRIES
@dp.callback_query_handler(text='rustic_fries')
async def rustic_fries(call: CallbackQuery):
    img = open('images/APPETIZERS/rustic fries.png', 'rb')
    txt = '<b>RUSTIC FRIES 14.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=rustic_friesbtn)
    await call.message.delete()

# APPETIZERS => NEXT BITES
@dp.callback_query_handler(text='next_bitesbtn')
async def back(call: CallbackQuery):
    img = open('images/APPETIZERS/bites.jpg', 'rb')
    txt = '<b>BITES 13.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=bitesbtn)
    await call.message.delete()

# APPETIZERS => BITES
@dp.callback_query_handler(text='bites')
async def bites(call: CallbackQuery):
    img = open('images/APPETIZERS/bites.jpg', 'rb')
    txt = '<b>BITES 13.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=bitesbtn)
    await call.message.delete()

# APPETIZERS => NEXT FRIENDS
@dp.callback_query_handler(text='next_friendsbtn')
async def friends(call: CallbackQuery):
    img = open('images/APPETIZERS/friends.jpg', 'rb')
    txt = '<b>FRIENDS 33.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=friendsbtn)
    await call.message.delete()

# APPETIZERS => FRIENDS
@dp.callback_query_handler(text='friends')
async def friends(call: CallbackQuery):
    img = open('images/APPETIZERS/friends.jpg', 'rb')
    txt = '<b>FRIENDS 33.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=friendsbtn)
    await call.message.delete()

# APPETIZERS => NEXT MUSHROOMS
@dp.callback_query_handler(text='next_mushroomsbtn')
async def strips1(call: CallbackQuery):
    img = open('images/APPETIZERS/mushrooms.jpg', 'rb')
    txt = '<b>MUSHROOMS 11.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=mushroomsbtn)
    await call.message.delete()

# APPETIZERS => MUSHROOMS
@dp.callback_query_handler(text='mushrooms')
async def strips1(call: CallbackQuery):
    img = open('images/APPETIZERS/mushrooms.jpg', 'rb')
    txt = '<b>MUSHROOMS 11.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=mushroomsbtn)
    await call.message.delete()

# APPETIZERS => NEXT TERIYAKI WINGS
@dp.callback_query_handler(text='next_teriyaki_wingsbtn')
async def teriyaki_wings3(call: CallbackQuery):
    img = open('images/APPETIZERS/teriyaki wings.jpg', 'rb')
    txt = '<b>TERIYAKI WINGS 3 PCS 19.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=teriyaki_wingsbtn)
    await call.message.delete()

# APPETIZERS => TERIYAKI WINGS
@dp.callback_query_handler(text='teriyaki_wings3')
async def teriyaki_wings3(call: CallbackQuery):
    img = open('images/APPETIZERS/teriyaki wings.jpg', 'rb')
    txt = '<b>TERIYAKI WINGS 3 PCS 19.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=teriyaki_wingsbtn)
    await call.message.delete()

# APPETIZERS => NEXT CHEESE NUGGETS
@dp.callback_query_handler(text='next_cheese_nuggetsbtn')
async def cheese_nuggets(call: CallbackQuery):
    img = open('images/APPETIZERS/cheese nuggets.jpg', 'rb')
    txt = '<b>CHEESE NUGGETS 14.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=cheese_nuggetsbtn)
    await call.message.delete()

# APPETIZERS => CHEESE NUGGETS
@dp.callback_query_handler(text='cheese_nuggets')
async def cheese_nuggets(call: CallbackQuery):
    img = open('images/APPETIZERS/cheese nuggets.jpg', 'rb')
    txt = '<b>CHEESE NUGGETS 14.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=cheese_nuggetsbtn)
    await call.message.delete()

# APPETIZERS => NEXT STRIPS
@dp.callback_query_handler(text='next_strips1btn')
async def strips1(call: CallbackQuery):
    img = open('images/APPETIZERS/strips1.jpg', 'rb')
    txt = '<b>STRIPS 1 PC 6.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=strips1btn)
    await call.message.delete()

# APPETIZERS => STRIPS
@dp.callback_query_handler(text='strips1')
async def strips1(call: CallbackQuery):
    img = open('images/APPETIZERS/strips1.jpg', 'rb')
    txt = '<b>STRIPS 1 PC 6.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=strips1btn)
    await call.message.delete()

# APPETIZERS => NEXT STRIPS 3
@dp.callback_query_handler(text='next_strips3btn')
async def strips3(call: CallbackQuery):
    img = open('images/APPETIZERS/strips3.jpg', 'rb')
    txt = '<b>STRIPS 3 PCS 15.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=strips3btn)
    await call.message.delete()

# APPETIZERS => STRIPS 3
@dp.callback_query_handler(text='strips3')
async def strips3(call: CallbackQuery):
    img = open('images/APPETIZERS/strips3.jpg', 'rb')
    txt = '<b>STRIPS 3 PCS 15.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=strips3btn)
    await call.message.delete()

# APPETIZERS => NEXT STRIPS 5
@dp.callback_query_handler(text='next_strips5btn')
async def strips5(call: CallbackQuery):
    img = open('images/APPETIZERS/strips 5.jpg', 'rb')
    txt = '<b>STRIPS 5 PCS 24.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=strips5btn)
    await call.message.delete()

# APPETIZERS => STRIPS 5
@dp.callback_query_handler(text='strips5')
async def strips5(call: CallbackQuery):
    img = open('images/APPETIZERS/strips 5.jpg', 'rb')
    txt = '<b>STRIPS 5 PCS 24.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=strips5btn)
    await call.message.delete()

# APPETIZERS => NEXT STRIPS 7
@dp.callback_query_handler(text='next_strips7btn')
async def strips7(call: CallbackQuery):
    img = open('images/APPETIZERS/strips 7.jpg', 'rb')
    txt = '<b>STRIPS 7 PCS 31.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=strips7btn)
    await call.message.delete()

# APPETIZERS => STRIPS 7
@dp.callback_query_handler(text='strips7')
async def strips7(call: CallbackQuery):
    img = open('images/APPETIZERS/strips 7.jpg', 'rb')
    txt = '<b>STRIPS 7 PCS 31.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=strips7btn)
    await call.message.delete()

# APPETIZERS => NEXT WINGS
@dp.callback_query_handler(text='next_wingsbtn')
async def wings1(call: CallbackQuery):
    img = open('images/APPETIZERS/wings1.jpg', 'rb')
    txt = '<b>WINGS 1 PC 6.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=wingsbtn)
    await call.message.delete()

# APPETIZERS => WINGS
@dp.callback_query_handler(text='wings1')
async def wings1(call: CallbackQuery):
    img = open('images/APPETIZERS/wings1.jpg', 'rb')
    txt = '<b>WINGS 1 PC 6.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=wingsbtn)
    await call.message.delete()

# APPETIZERS => NEXT HOT WINGS 3
@dp.callback_query_handler(text='next_hot_wings3btn')
async def hot_wings3(call: CallbackQuery):
    img = open('images/APPETIZERS/hot wings 3.jpg', 'rb')
    txt = '<b>HOT WINGS 3 PCS 18.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=hot_wings3btn)
    await call.message.delete()

# APPETIZERS => HOT WINGS 3
@dp.callback_query_handler(text='hot_wings3')
async def hot_wings3(call: CallbackQuery):
    img = open('images/APPETIZERS/hot wings 3.jpg', 'rb')
    txt = '<b>HOT WINGS 3 PCS 18.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=hot_wings3btn)
    await call.message.delete()

# APPETIZERS => NEXT HOT WINGS 5
@dp.callback_query_handler(text='next_hot_wings5btn')
async def hot_wings5(call: CallbackQuery):
    img = open('images/APPETIZERS/hot wings 5.jpg', 'rb')
    txt = '<b>HOT WINGS 5 PCS 28.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=hot_wings5btn)
    await call.message.delete()

# APPETIZERS => HOT WINGS 5
@dp.callback_query_handler(text='hot_wings5')
async def hot_wings5(call: CallbackQuery):
    img = open('images/APPETIZERS/hot wings 5.jpg', 'rb')
    txt = '<b>HOT WINGS 5 PCS 28.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=hot_wings5btn)
    await call.message.delete()

# APPETIZERS => NEXT HOT WINGS 7
@dp.callback_query_handler(text='next_hot_wings7btn')
async def hot_wings7(call: CallbackQuery):
    img = open('images/APPETIZERS/hot wings 7.jpg', 'rb')
    txt = '<b>HOT WINGS 7 PCS 38.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=hot_wings7btn)
    await call.message.delete()
# APPETIZERS => HOT WINGS 7
@dp.callback_query_handler(text='hot_wings7')
async def hot_wings7(call: CallbackQuery):
    img = open('images/APPETIZERS/hot wings 7.jpg', 'rb')
    txt = '<b>HOT WINGS 7 PCS 38.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=hot_wings7btn)
    await call.message.delete()

# APPETIZERS => NEXT CHECHEVIT SOUP
@dp.callback_query_handler(text='next_chechevit_soupbtn')
async def chechevit_soup(call: CallbackQuery):
    img = open('images/APPETIZERS/chechevit soup.jpg', 'rb')
    txt = '<b>CHECHEVIT SOUP 10.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=chechevit_soupbtn)
    await call.message.delete()

# APPETIZERS => CHECHEVIT SOUP
@dp.callback_query_handler(text='chechevit_soup')
async def chechevit_soup(call: CallbackQuery):
    img = open('images/APPETIZERS/chechevit soup.jpg', 'rb')
    txt = '<b>CHECHEVIT SOUP 10.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=chechevit_soupbtn)
    await call.message.delete()

# BURGERS
@dp.callback_query_handler(text='burgers')
async def burgers(call: CallbackQuery):
    await call.message.answer('<b>BURGERS MENU</b>', parse_mode='html', reply_markup=burgersMenu)
    await call.message.delete()
    await call.answer(cache_time=30)

# BURGERS => CLASSIC
@dp.callback_query_handler(text='classic')
async def classic(call: CallbackQuery):
    img = open('images/BURGERS/classic.jpg', 'rb')
    txt = '<b>CLASSIC 19.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=classic_btn)
    await call.message.delete()

# BURGERS => NEXT LONGER
@dp.callback_query_handler(text='next_longer_btn')
async def longer(call: CallbackQuery):
    img = open('images/BURGERS/longer.jpg', 'rb')
    txt = '<b>LONGER 19.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=longer_btn)
    await call.message.delete()

# BURGERS => LONGER
@dp.callback_query_handler(text='longer')
async def longer(call: CallbackQuery):
    img = open('images/BURGERS/longer.jpg', 'rb')
    txt = '<b>LONGER 19.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=longer_btn)
    await call.message.delete()

# BURGERS => NEXT BIGGER
@dp.callback_query_handler(text='next_bigger_btn')
async def bigger(call: CallbackQuery):
    img = open('images/BURGERS/bigger.jpg', 'rb')
    txt = '<b>BIGGER 23.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=bigger_btn)
    await call.message.delete()

# BURGERS => BIGGER
@dp.callback_query_handler(text='bigger')
async def bigger(call: CallbackQuery):
    img = open('images/BURGERS/bigger.jpg', 'rb')
    txt = '<b>BIGGER 23.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=bigger_btn)
    await call.message.delete()

# BURGERS => NEXT CHILI LONGER
@dp.callback_query_handler(text='next_chili_longer_btn')
async def chili_longer(call: CallbackQuery):
    img = open('images/BURGERS/chili longer.jpg', 'rb')
    txt = '<b>CHILI LONGER 24.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=chili_longer_btn)
    await call.message.delete()

# BURGERS => CHILI LONGER
@dp.callback_query_handler(text='chili_longer')
async def chili_longer(call: CallbackQuery):
    img = open('images/BURGERS/chili longer.jpg', 'rb')
    txt = '<b>CHILI LONGER 24.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=chili_longer_btn)
    await call.message.delete()

# BURGERS => NEXT BEEF LONGER
@dp.callback_query_handler(text='next_beef_longer_btn')
async def beef_longer(call: CallbackQuery):
    img = open('images/BURGERS/beef longer.jpg', 'rb')
    txt = '<b>BEEF LONGER 24.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=beef_longer_btn)
    await call.message.delete()

# BURGERS => BEEF LONGER
@dp.callback_query_handler(text='beef_longer')
async def beef_longer(call: CallbackQuery):
    img = open('images/BURGERS/beef longer.jpg', 'rb')
    txt = '<b>BEEF LONGER 24.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=beef_longer_btn)
    await call.message.delete()

# BURGERS => NEXT CHEESY BURGER
@dp.callback_query_handler(text='next_cheesy_burger_btn')
async def cheesy_burger(call: CallbackQuery):
    img = open('images/BURGERS/cheesy burger.jpg', 'rb')
    txt = '<b>CHEESY BURGER 32.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=cheesy_burger_btn)
    await call.message.delete()
# BURGERS => CHEESY BURGER
@dp.callback_query_handler(text='cheesy_burger')
async def cheesy_burger(call: CallbackQuery):
    img = open('images/BURGERS/cheesy burger.jpg', 'rb')
    txt = '<b>CHEESY BURGER 32.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=cheesy_burger_btn)
    await call.message.delete()

# BURGERS => NEXT JUNIOR BURGER
@dp.callback_query_handler(text='next_junior_burger_btn')
async def junior_burger(call: CallbackQuery):
    img = open('images/BURGERS/junior.jpg', 'rb')
    txt = '<b>JUNIOR BURGER 16.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=junior_burger_btn)
    await call.message.delete()

# BURGERS => JUNIOR BURGER
@dp.callback_query_handler(text='junior_burger')
async def junior_burger(call: CallbackQuery):
    img = open('images/BURGERS/classic.jpg', 'rb')
    txt = '<b>JUNIOR BURGER 16.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=junior_burger_btn)
    await call.message.delete()

# BURGERS => NEXT HAMBURGER
@dp.callback_query_handler(text='next_hamburger_btn')
async def hamburger(call: CallbackQuery):
    img = open('images/BURGERS/hamburger.jpg', 'rb')
    txt = '<b>HAMBURGER 25.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=hamburger_btn)
    await call.message.delete()

# BURGERS => HAMBURGER
@dp.callback_query_handler(text='hamburger')
async def hamburger(call: CallbackQuery):
    img = open('images/BURGERS/hamburger.jpg', 'rb')
    txt = '<b>HAMBURGER 25.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=hamburger_btn)
    await call.message.delete()

# BURGERS => NEXT CHEESE BURGER
@dp.callback_query_handler(text='next_cheese_burger_btn')
async def cheese_burger(call: CallbackQuery):
    img = open('images/BURGERS/cheese burger.jpg', 'rb')
    txt = '<b>CHEESE BURGER 28.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=cheese_burger_btn)
    await call.message.delete()

# BURGERS => CHEESE BURGER
@dp.callback_query_handler(text='cheese_burger')
async def cheese_burger(call: CallbackQuery):
    img = open('images/BURGERS/cheese burger.jpg', 'rb')
    txt = '<b>CHEESE BURGER 28.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=cheese_burger_btn)
    await call.message.delete()

# BURGERS => NEXT BARBECUE BURGER
@dp.callback_query_handler(text='next_barbecue_burger_btn')
async def barbecue_burger(call: CallbackQuery):
    img = open('images/BURGERS/barbecue burger.jpg', 'rb')
    txt = '<b>BARBECUE BURGER 27.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=barbecue_burger_btn)
    await call.message.delete()

# BURGERS => BARBECUE BURGER
@dp.callback_query_handler(text='barbecue_burger')
async def barbecue_burger(call: CallbackQuery):
    img = open('images/BURGERS/barbecue burger.jpg', 'rb')
    txt = '<b>BARBECUE BURGER 27.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=barbecue_burger_btn)
    await call.message.delete()

# BURGERS => NEXT CHICKY BURGER
@dp.callback_query_handler(text='next_chicky_burger_btn')
async def chicky_burger(call: CallbackQuery):
    img = open('images/BURGERS/chicky burger.jpg', 'rb')
    txt = '<b>CHICKY BURGER 18.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=chicky_burger_btn)
    await call.message.delete()

# BURGERS => CHICKY BURGER
@dp.callback_query_handler(text='chicky_burger')
async def chicky_burger(call: CallbackQuery):
    img = open('images/BURGERS/chicky burger.jpg', 'rb')
    txt = '<b>CHICKY BURGER 18.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=chicky_burger_btn)
    await call.message.delete()

# BURGERS => NEXT ROAST BURGER
@dp.callback_query_handler(text='next_roast_burger_btn')
async def roast_burger(call: CallbackQuery):
    img = open('images/BURGERS/roast burger.jpg', 'rb')
    txt = '<b>ROAST BURGER 25.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=roast_burger_btn)
    await call.message.delete()

# BURGERS => ROAST BURGER
@dp.callback_query_handler(text='roast_burger')
async def roast_burger(call: CallbackQuery):
    img = open('images/BURGERS/roast burger.jpg', 'rb')
    txt = '<b>ROAST BURGER 25.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=roast_burger_btn)
    await call.message.delete()

# BURGERS => NEXT DOUBLE CHEESE BURGER
@dp.callback_query_handler(text='next_double_cheese_burger_btn')
async def double_cheese_longer(call: CallbackQuery):
    img = open('images/BURGERS/double cheese burger.jpg', 'rb')
    txt = '<b>DOUBLE CHEESE BURGER 39.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=double_cheese_burger_btn)
    await call.message.delete()

# BURGERS => DOUBLE CHEESE BURGER
@dp.callback_query_handler(text='double_cheese_burger')
async def double_cheese_longer(call: CallbackQuery):
    img = open('images/BURGERS/double cheese burger.jpg', 'rb')
    txt = '<b>DOUBLE CHEESE BURGER 39.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=double_cheese_burger_btn)
    await call.message.delete()


# PIZZA
@dp.callback_query_handler(text='pizza')
async def pizza(call: CallbackQuery):
    await call.message.answer('<b>PIZZA MENU</b>', parse_mode='html', reply_markup=pizzaMenu)
    await call.message.delete()
    await call.answer(cache_time=30)

# PIZZA => NEXT PIZZA SUPREME
@dp.callback_query_handler(text='pizza_supreme')
async def pizza_supreme(call: CallbackQuery):
    img = open('images/PIZZA/PIZZA SUPREME.jpg', 'rb')
    txt = '<b>PIZZA SUPREME 48.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=pizza_supreme_btn)
    await call.message.delete()

# PIZZA => PIZZA SUPREME
@dp.callback_query_handler(text='pizza_supreme')
async def pizza_supreme(call: CallbackQuery):
    img = open('images/PIZZA/PIZZA SUPREME.jpg', 'rb')
    txt = '<b>PIZZA SUPREME 48.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=pizza_supreme_btn)
    await call.message.delete()

# PIZZA => NEXT PIZZA SPICY
@dp.callback_query_handler(text='next_pizza_spicy_btn')
async def pizza_spicy(call: CallbackQuery):
    img = open('images/PIZZA/PIZZA SPICY.jpg', 'rb')
    txt = '<b>PIZZA SPICY 43.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=pizza_spicy_btn)
    await call.message.delete()

# PIZZA => PIZZA SPICY
@dp.callback_query_handler(text='pizza_spicy')
async def pizza_spicy(call: CallbackQuery):
    img = open('images/PIZZA/PIZZA SPICY.jpg', 'rb')
    txt = '<b>PIZZA SPICY 43.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=pizza_spicy_btn)
    await call.message.delete()

# PIZZA => NEXT PIZZA VEGETARIAN
@dp.callback_query_handler(text='next_pizza_vegetarian_btn')
async def pizza_vegetarian(call: CallbackQuery):
    img = open('images/PIZZA/PIZZA VEGETARIAN.jpg', 'rb')
    txt = '<b>PIZZA VEGETARIAN 39.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=pizza_vegetarian_btn)
    await call.message.delete()

# PIZZA => PIZZA VEGETARIAN
@dp.callback_query_handler(text='pizza_vegetarian')
async def pizza_vegetarian(call: CallbackQuery):
    img = open('images/PIZZA/PIZZA VEGETARIAN.jpg', 'rb')
    txt = '<b>PIZZA VEGETARIAN 39.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=pizza_vegetarian_btn)
    await call.message.delete()

# PIZZA => NEXT PIZZA HAWAIIAN
@dp.callback_query_handler(text='next_pizza_hawaiian_btn')
async def pizza_hawaiian(call: CallbackQuery):
    img = open('images/PIZZA/PIZZA HAWAIIAN.jpg', 'rb')
    txt = '<b>PIZZA HAWAIIAN 34.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=pizza_hawaiian_btn)
    await call.message.delete()

# PIZZA => PIZZA HAWAIIAN
@dp.callback_query_handler(text='pizza_hawaiian')
async def pizza_hawaiian(call: CallbackQuery):
    img = open('images/PIZZA/PIZZA HAWAIIAN.jpg', 'rb')
    txt = '<b>PIZZA HAWAIIAN 34.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=pizza_hawaiian_btn)
    await call.message.delete()

# PIZZA => NEXT PIZZA MARGARITA
@dp.callback_query_handler(text='next_pizza_margarita_btn')
async def pizza_margarita(call: CallbackQuery):
    img = open('images/PIZZA/PIZZA MARGARITA.jpg', 'rb')
    txt = '<b>PIZZA MARGARITA 36.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=pizza_margarita_btn)
    await call.message.delete()

# PIZZA => PIZZA MARGARITA
@dp.callback_query_handler(text='pizza_margarita')
async def pizza_margarita(call: CallbackQuery):
    img = open('images/PIZZA/PIZZA MARGARITA.jpg', 'rb')
    txt = '<b>PIZZA MARGARITA 36.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=pizza_margarita_btn)
    await call.message.delete()

# PIZZA => NEXT PIZZA STEAK
@dp.callback_query_handler(text='next_pizza_steak_btn')
async def pizza_steak(call: CallbackQuery):
    img = open('images/PIZZA/PIZZA STEAK.jpg', 'rb')
    txt = '<b>PIZZA STEAK 55.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=pizza_steak_btn)
    await call.message.delete()

# PIZZA => PIZZA STEAK
@dp.callback_query_handler(text='pizza_steak')
async def pizza_steak(call: CallbackQuery):
    img = open('images/PIZZA/PIZZA STEAK.jpg', 'rb')
    txt = '<b>PIZZA STEAK 55.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=pizza_steak_btn)
    await call.message.delete()

# PIZZA => NEXT PIZZA BBQ CHICKEN
@dp.callback_query_handler(text='next_pizza_bbqchicken_btn')
async def pizza_bbq_chicken(call: CallbackQuery):
    img = open('images/PIZZA/PIZZA BBQ CHICKEN.jpg', 'rb')
    txt = '<b>PIZZA BBQ CHICKEN 39.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=pizza_bbqchicken_btn)
    await call.message.delete()

# PIZZA => PIZZA BBQ CHICKEN
@dp.callback_query_handler(text='pizza_bbq_chicken')
async def pizza_bbq_chicken(call: CallbackQuery):
    img = open('images/PIZZA/PIZZA BBQ CHICKEN.jpg', 'rb')
    txt = '<b>PIZZA BBQ CHICKEN 39.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=pizza_bbqchicken_btn)
    await call.message.delete()

# PIZZA => NEXT PIZZA WHITE CHEESE
@dp.callback_query_handler(text='next_pizza_whitecheese_btn')
async def pizza_white_cheese(call: CallbackQuery):
    img = open('images/PIZZA/PIZZA WHITE CHEESE.jpg', 'rb')
    txt = '<b>PIZZA WHITE CHEESE 33.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=pizza_whitecheese_btn)
    await call.message.delete()

# PIZZA => PIZZA WHITE CHEESE
@dp.callback_query_handler(text='pizza_white_cheese')
async def pizza_white_cheese(call: CallbackQuery):
    img = open('images/PIZZA/PIZZA WHITE CHEESE.jpg', 'rb')
    txt = '<b>PIZZA WHITE CHEESE 33.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=pizza_whitecheese_btn)
    await call.message.delete()

# PIZZA => NEXT PIZZA PEPPERONI
@dp.callback_query_handler(text='next_pizza_pepperoni_btn')
async def pizza_pepperoni(call: CallbackQuery):
    img = open('images/PIZZA/PIZZA PEPPERONI.jpg', 'rb')
    txt = '<b>PIZZA PEPPERONI 38.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=pizza_pepperoni_btn)
    await call.message.delete()

# PIZZA => PIZZA PEPPERONI
@dp.callback_query_handler(text='pizza_pepperoni')
async def pizza_pepperoni(call: CallbackQuery):
    img = open('images/PIZZA/PIZZA PEPPERONI.jpg', 'rb')
    txt = '<b>PIZZA PEPPERONI 38.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=pizza_pepperoni_btn)
    await call.message.delete()

# PIZZA => NEXT PIZZA FRANKFURT
@dp.callback_query_handler(text='next_pizza_frankfurt_btn')
async def pizza_frankfurt(call: CallbackQuery):
    img = open('images/PIZZA/PIZZA FRANKFURT.jpg', 'rb')
    txt = '<b>PIZZA FRANKFURT 38.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=pizza_frankfurt_btn)
    await call.message.delete()

# PIZZA => PIZZA FRANKFURT
@dp.callback_query_handler(text='pizza_frankfurt')
async def pizza_frankfurt(call: CallbackQuery):
    img = open('images/PIZZA/PIZZA FRANKFURT.jpg', 'rb')
    txt = '<b>PIZZA FRANKFURT 38.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=pizza_frankfurt_btn)
    await call.message.delete()

# SPINNER
@dp.callback_query_handler(text='spinner')
async def spinner(call: CallbackQuery):
    await call.message.answer('<b>SPINNER MENU</b>', parse_mode='html', reply_markup=spinnerMenu)
    await call.message.delete()
    await call.answer(cache_time=30)

# SPINNER => SPINNER SNACK
@dp.callback_query_handler(text='spinner_snack')
async def spinner_snack(call: CallbackQuery):
    img = open('images/SPINNER/SPINNER SNACK.jpg', 'rb')
    txt = '<b>SPINNER SNACK 19.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=spinner_snack_btn)
    await call.message.delete()

# SPINNER => NEXT SPINNER TAKO
@dp.callback_query_handler(text='next_spinner_tako_btn')
async def spinner_tako(call: CallbackQuery):
    img = open('images/SPINNER/SPINNER TAKO.jpg', 'rb')
    txt = '<b>SPINNER TAKO 19.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=spinner_tako_btn)
    await call.message.delete()

# SPINNER => SPINNER TAKO
@dp.callback_query_handler(text='spinner_tako')
async def spinner_tako(call: CallbackQuery):
    img = open('images/SPINNER/SPINNER TAKO.jpg', 'rb')
    txt = '<b>SPINNER TAKO 19.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=spinner_tako_btn)
    await call.message.delete()

# SPINNER => NEXT SPINNER SALSA
@dp.callback_query_handler(text='next_spinner_salsa_btn')
async def spinner_salsa(call: CallbackQuery):
    img = open('images/SPINNER/SPINNER SALSA.jpg', 'rb')
    txt = '<b>SPINNER SALSA 19.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=spinner_salsa_btn)
    await call.message.delete()

# SPINNER => SPINNER SALSA
@dp.callback_query_handler(text='spinner_salsa')
async def spinner_salsa(call: CallbackQuery):
    img = open('images/SPINNER/SPINNER SALSA.jpg', 'rb')
    txt = '<b>SPINNER SALSA 19.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=spinner_salsa_btn)
    await call.message.delete()

# SPINNER =>  NEXT SPINNER NO SOUCE
@dp.callback_query_handler(text='next_spinner_nosouce_btn')
async def spinner_no_souce(call: CallbackQuery):
    img = open('images/SPINNER/SPINNER NO SOUCE.jpg', 'rb')
    txt = '<b>SPINNER NO SOUCE 19.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=spinner_nosouce_btn)
    await call.message.delete()

# SPINNER => SPINNER NO SOUCE
@dp.callback_query_handler(text='spinner_no_souce')
async def spinner_no_souce(call: CallbackQuery):
    img = open('images/SPINNER/SPINNER NO SOUCE.jpg', 'rb')
    txt = '<b>SPINNER NO SOUCE 19.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=spinner_nosouce_btn)
    await call.message.delete()

# SPINNER => NEXT DUET MASTER
@dp.callback_query_handler(text='next_duet_master_btn')
async def duet_master(call: CallbackQuery):
    img = open('images/SPINNER/DUET MASTER.jpg', 'rb')
    txt = '<b>DUET MASTER 26.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=duet_master_btn)
    await call.message.delete()

# SPINNER => DUET MASTER
@dp.callback_query_handler(text='duet_master')
async def duet_master(call: CallbackQuery):
    img = open('images/SPINNER/DUET MASTER.jpg', 'rb')
    txt = '<b>DUET MASTER 26.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=duet_master_btn)
    await call.message.delete()


# SPINNER => NEXT SMILE BOX
@dp.callback_query_handler(text='next_smile_box_btn')
async def smile_box(call: CallbackQuery):
    img = open('images/SPINNER/SMILE BOX.jpg', 'rb')
    txt = '<b>SMILE BOX 26.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=smile_box_btn)
    await call.message.delete()

# SPINNER => SMILE BOX
@dp.callback_query_handler(text='smile_box')
async def smile_box(call: CallbackQuery):
    img = open('images/SPINNER/SMILE BOX.jpg', 'rb')
    txt = '<b>SMILE BOX 26.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=smile_box_btn)
    await call.message.delete()

# SPINNER => NEXT SPINNER SUPER CHARGED
@dp.callback_query_handler(text='next_spinner_super_charged_btn')
async def spinner_super_charged(call: CallbackQuery):
    img = open('images/SPINNER/SPINNER SUPER CHARGED.jpg', 'rb')
    txt = '<b>SPINNER SUPER CHARGED 19.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=spinner_super_charged_btn)
    await call.message.delete()


# SPINNER => SPINNER SUPER CHARGED
@dp.callback_query_handler(text='spinner_super_charged')
async def spinner_super_charged(call: CallbackQuery):
    img = open('images/SPINNER/SPINNER SUPER CHARGED.jpg', 'rb')
    txt = '<b>SPINNER SUPER CHARGED 19.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=spinner_super_charged_btn)
    await call.message.delete()


# CHICKEN
@dp.callback_query_handler(text='chicken')
async def chicken(call: CallbackQuery):
    await call.message.answer('<b>CHICKEN MENU</b>', parse_mode='html', reply_markup=chickenMenu)
    await call.message.delete()
    await call.answer(cache_time=30)

# CHICKEN => CHICKEN SPICY
@dp.callback_query_handler(text='chicken_spicy')
async def chicken1_spicy(call: CallbackQuery):
    img = open('images/CHICKEN/CHICKEN 1 PCS SPICY.jpg', 'rb')
    txt = '<b>CHICKEN 1 PC SPICY 10.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=chicken_spicy_btn)
    await call.message.delete()

# CHICKEN => NEXT CHICKEN NORMAL
@dp.callback_query_handler(text='next_chicken_normal_btn')
async def chicken1_normal(call: CallbackQuery):
    img = open('images/CHICKEN/CHICKEN 1 PCS NORMAL.jpg', 'rb')
    txt = '<b>CHICKEN 1 PC NORMAL 10.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=chicken_normal_btn)
    await call.message.delete()

# CHICKEN => CHICKEN NORMAL
@dp.callback_query_handler(text='chicken_normal')
async def chicken1_normal(call: CallbackQuery):
    img = open('images/CHICKEN/CHICKEN 1 PCS NORMAL.jpg', 'rb')
    txt = '<b>CHICKEN 1 PC NORMAL 10.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=chicken_normal_btn)
    await call.message.delete()

# CHICKEN => NEXT SNACK MEAL SPICY
@dp.callback_query_handler(text='next_snack_meal_spicy_btn')
async def snack_meal_spicy(call: CallbackQuery):
    img = open('images/CHICKEN/SNACK MEAL SPICY.jpg', 'rb')
    txt = '<b>SNACK MEAL SPICY 29.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=snack_meal_spicy_btn)
    await call.message.delete()

# CHICKEN => SNACK MEAL SPICY
@dp.callback_query_handler(text='snack_meal_spicy')
async def snack_meal_spicy(call: CallbackQuery):
    img = open('images/CHICKEN/SNACK MEAL NORMAL.jpg', 'rb')
    txt = '<b>SNACK MEAL NORMAL 29.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=snack_meal_spicy_btn)
    await call.message.delete()

# CHICKEN => NEXT SNACK MEAL NORMAL
@dp.callback_query_handler(text='next_snack_meal_normal_btn')
async def snack_meal_normal(call: CallbackQuery):
    img = open('images/CHICKEN/SNACK MEAL NORMAL.jpg', 'rb')
    txt = '<b>SNACK MEAL NORMAL 29.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=snack_meal_normal_btn)
    await call.message.delete()

# CHICKEN => SNACK MEAL NORMAL
@dp.callback_query_handler(text='snack_meal_normal')
async def snack_meal_normal(call: CallbackQuery):
    img = open('images/CHICKEN/SNACK MEAL NORMAL.jpg', 'rb')
    txt = '<b>SNACK MEAL NORMAL 29.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=snack_meal_normal_btn)
    await call.message.delete()

# CHICKEN => NEXT DINNER MEAL SPICY
@dp.callback_query_handler(text='next_dinner_meal_spicy_btn')
async def dinner_meal_normal(call: CallbackQuery):
    img = open('images/CHICKEN/DINNER MEAL SPICY.jpg', 'rb')
    txt = '<b>DINNER MEAL SPICY 38.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=dinner_meal_spicy_btn)
    await call.message.delete()

# CHICKEN => DINNER MEAL SPICY
@dp.callback_query_handler(text='dinner_meal_spicy')
async def dinner_meal_normal(call: CallbackQuery):
    img = open('images/CHICKEN/DINNER MEAL SPICY.jpg', 'rb')
    txt = '<b>DINNER MEAL SPICY 38.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=dinner_meal_spicy_btn)
    await call.message.delete()

# CHICKEN => NEXT DINNER MEAL NORMAL
@dp.callback_query_handler(text='next_dinner_meal_normal_btn')
async def dinner_meal_spicy(call: CallbackQuery):
    img = open('images/CHICKEN/DINNER MEAL NORMAL.jpg', 'rb')
    txt = '<b>DINNER MEAL NORMAL 38.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=dinner_meal_normal_btn)
    await call.message.delete()

# CHICKEN => DINNER MEAL NORMAL
@dp.callback_query_handler(text='dinner_meal_normal')
async def dinner_meal_spicy(call: CallbackQuery):
    img = open('images/CHICKEN/DINNER MEAL NORMAL.jpg', 'rb')
    txt = '<b>DINNER MEAL NORMAL 38.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=dinner_meal_normal_btn)
    await call.message.delete()

# CHICKEN => NEXT DOUBLE MEAL
@dp.callback_query_handler(text='next_double_meal_btn')
async def mix_meal_normal(call: CallbackQuery):
    img = open('images/CHICKEN/DOUBLE MEAL.jpg', 'rb')
    txt = '<b>DOUBLE MEAL 55.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=double_meal_btn)
    await call.message.delete()

# CHICKEN => DOUBLE MEAL
@dp.callback_query_handler(text='double_meal_normal')
async def mix_meal_normal(call: CallbackQuery):
    img = open('images/CHICKEN/DOUBLE MEAL.jpg', 'rb')
    txt = '<b>DOUBLE MEAL 55.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=double_meal_btn)
    await call.message.delete()

# CHICKEN => NEXT MIX MEAL
@dp.callback_query_handler(text='next_mix_meal_normal_btn')
async def double_meal(call: CallbackQuery):
    img = open('images/CHICKEN/MIX MEAL (normal).jpg', 'rb')
    txt = '<b>MIX MEAL NORMAL 29.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=mix_meal_normal_btn)
    await call.message.delete()

# CHICKEN => NEXT MIX MEAL
@dp.callback_query_handler(text='mix_meal')
async def double_meal(call: CallbackQuery):
    img = open('images/CHICKEN/MIX MEAL (normal).jpg', 'rb')
    txt = '<b>MIX MEAL NORMAL 29.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=mix_meal_normal_btn)
    await call.message.delete()

# CHICKEN => NEXT CHICKEN SET 12PCS SPICY
@dp.callback_query_handler(text='next_chicken_set_spicy_btn')
async def chicken12_set_normal(call: CallbackQuery):
    img = open('images/CHICKEN/CHICKEN 1 PCS SPICY.jpg', 'rb')
    txt = '<b>CHICKEN 1 PCS SPICY 149.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=chicken_set_spicy_btn)
    await call.message.delete()

# CHICKEN => CHICKEN SET 12PCS SPICY
@dp.callback_query_handler(text='chicken_set_spicy')
async def chicken12_set_normal(call: CallbackQuery):
    img = open('images/CHICKEN/CHICKEN 1 PCS SPICY.jpg', 'rb')
    txt = '<b>CHICKEN 1 PCS SPICY 149.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=chicken_set_spicy_btn)
    await call.message.delete()


# CHICKEN => NEXT CHICKEN SET 12PCS NORMAL
@dp.callback_query_handler(text='chicken_set_normal')
async def chicken12_set_spicy(call: CallbackQuery):
    img = open('images/CHICKEN/CHICKEN 1 PCS NORMAL.jpg', 'rb')
    txt = '<b>CHICKEN 1 PCS NORMAL 149.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=chicken_set_normal_btn)
    await call.message.delete()

# CHICKEN => CHICKEN SET 12PCS NORMAL
@dp.callback_query_handler(text='chicken_set_normal')
async def chicken12_set_spicy(call: CallbackQuery):
    img = open('images/CHICKEN/CHICKEN 1 PCS NORMAL.jpg', 'rb')
    txt = '<b>CHICKEN 1 PCS NORMAL 149.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=chicken_set_normal_btn)
    await call.message.delete()

# SALADS AND OTHER
@dp.callback_query_handler(text='salads')
async def salads(call: CallbackQuery):
    await call.message.answer('<b>SALADS AND OTHER MENU</b>', parse_mode='html', reply_markup=saladMenu)
    await call.message.delete()
    await call.answer(cache_time=30)

# SALADS AND OTHER => COLESLAW SALAD
@dp.callback_query_handler(text='coleslaw_salad')
async def coleslaw_salad(call: CallbackQuery):
    img = open('images/SALADS AND OTHER/COLESLAW SALAD.jpg', 'rb')
    txt = '<b>COLESLAW SALAD 5.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=coleslaw_salad_btn)
    await call.message.delete()

# SALADS AND OTHER => NEXT LOOOK SALAD
@dp.callback_query_handler(text='next_loook_salad_btn')
async def loook_salad(call: CallbackQuery):
    img = open('images/SALADS AND OTHER/LOOOK SALAD.png', 'rb')
    txt = '<b>LOOOK SALAD 11.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=loook_salad_btn)
    await call.message.delete()

# SALADS AND OTHER => LOOOK SALAD
@dp.callback_query_handler(text='loook_salad')
async def loook_salad(call: CallbackQuery):
    img = open('images/SALADS AND OTHER/LOOOK SALAD.png', 'rb')
    txt = '<b>LOOOK SALAD 11.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=loook_salad_btn)
    await call.message.delete()

# SALADS AND OTHER => NEXT VEGGIE FRESH SALAD
@dp.callback_query_handler(text='next_veggie_fresh_salad_btn')
async def veggie_fresh_salad(call: CallbackQuery):
    img = open('images/SALADS AND OTHER/VEGGIE FRESH SALAD.jpg', 'rb')
    txt = '<b>VEGGIE FRESH SALAD 13.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=veggie_fresh_salad_btn)
    await call.message.delete()

# SALADS AND OTHER => VEGGIE FRESH SALAD
@dp.callback_query_handler(text='veggie_fresh_salad')
async def veggie_fresh_salad(call: CallbackQuery):
    img = open('images/SALADS AND OTHER/VEGGIE FRESH SALAD.jpg', 'rb')
    txt = '<b>VEGGIE FRESH SALAD 13.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=veggie_fresh_salad_btn)
    await call.message.delete()

# SALADS AND OTHER => NEXT BREAD PIKELET
@dp.callback_query_handler(text='next_bread_pikelet_btn')
async def bread_pikelet(call: CallbackQuery):
    img = open('images/SALADS AND OTHER/BREAD PIKELET.jpg', 'rb')
    txt = '<b>BREAD PIKELET 2.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=bread_pikelet_btn)
    await call.message.delete()

# SALADS AND OTHER => BREAD PIKELET
@dp.callback_query_handler(text='bread_pikelet')
async def bread_pikelet(call: CallbackQuery):
    img = open('images/SALADS AND OTHER/BREAD PIKELET.jpg', 'rb')
    txt = '<b>BREAD PIKELET 2.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=bread_pikelet_btn)
    await call.message.delete()


# DESSERTS
@dp.callback_query_handler(text='desserts')
async def desserts(call: CallbackQuery):
    await call.message.answer('<b>DESSERTS MENU</b>', parse_mode='html', reply_markup=dessertMenu)
    await call.message.delete()
    await call.answer(cache_time=30)

# DESSERTS => RED WAVE
@dp.callback_query_handler(text='red_wave')
async def red_wave(call: CallbackQuery):
    img = open('images/DESSERTS/RED WAVE.jpg', 'rb')
    txt = '<b>RED WAVE 13.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=red_wave_btn)
    await call.message.delete()

#DESSERTS => NEXT LEMON CAKE
@dp.callback_query_handler(text='next_lemon_cake_btn')
async def lemon_cake(call: CallbackQuery):
    img = open('images/DESSERTS/LEMON CAKE.jpg', 'rb')
    txt = '<b>LEMON CAKE 10.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=lemon_cake_btn)
    await call.message.delete()

#DESSERTS => LEMON CAKE
@dp.callback_query_handler(text='lemon_cake')
async def lemon_cake(call: CallbackQuery):
    img = open('images/DESSERTS/LEMON CAKE.jpg', 'rb')
    txt = '<b>LEMON CAKE 10.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=lemon_cake_btn)
    await call.message.delete()

#DESSERTS => NEXT KIWIX
@dp.callback_query_handler(text='next_kiwix_btn')
async def kiwix(call: CallbackQuery):
    img = open('images/DESSERTS/KIWIX.jpg', 'rb')
    txt = '<b>KIWIX 13.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=kiwix_btn)
    await call.message.delete()

#DESSERTS => KIWIX
@dp.callback_query_handler(text='kiwix')
async def kiwix(call: CallbackQuery):
    img = open('images/DESSERTS/KIWIX.jpg', 'rb')
    txt = '<b>KIWIX 13.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=kiwix_btn)
    await call.message.delete()

#DESSERTS => NEXT CHOCOTASTIC
@dp.callback_query_handler(text='next_chocotastic_btn')
async def chocotastic(call: CallbackQuery):
    img = open('images/DESSERTS/CHOCOTASTIC.jpg', 'rb')
    txt = '<b>CHOCOTASTIC 13.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=chocotastic_btn)
    await call.message.delete()

#DESSERTS => CHOCOTASTIC
@dp.callback_query_handler(text='chocotastic')
async def chocotastic(call: CallbackQuery):
    img = open('images/DESSERTS/CHOCOTASTIC.jpg', 'rb')
    txt = '<b>CHOCOTASTIC 13.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=chocotastic_btn)
    await call.message.delete()

#DESSERTS => NEXT TELLO
@dp.callback_query_handler(text='next_tello_btn')
async def tello(call: CallbackQuery):
    img = open('images/DESSERTS/TELLO.jpg', 'rb')
    txt = '<b>TELLO 15.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=tello_btn)
    await call.message.delete()

#DESSERTS => TELLO
@dp.callback_query_handler(text='tello')
async def tello(call: CallbackQuery):
    img = open('images/DESSERTS/TELLO.jpg', 'rb')
    txt = '<b>TELLO 15.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=tello_btn)
    await call.message.delete()

#DESSERTS => NEXT SUGAR CHIP
@dp.callback_query_handler(text='next_sugar_chip_btn')
async def sugar_chip(call: CallbackQuery):
    img = open('images/DESSERTS/SUGAR CHIP 1PCS.jpg', 'rb')
    txt = '<b>SUGAR CHIP 1PC 2.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=sugar_chip_btn)
    await call.message.delete()

#DESSERTS => SUGAR CHIP
@dp.callback_query_handler(text='sugar_chip')
async def sugar_chip(call: CallbackQuery):
    img = open('images/DESSERTS/SUGAR CHIP 1PCS.jpg', 'rb')
    txt = '<b>SUGAR CHIP 1PC 2.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=sugar_chip_btn)
    await call.message.delete()

#DESSERTS => NEXT CHOCOLATE SOUFFLE
@dp.callback_query_handler(text='next_chocolate_souffle_btn')
async def chocolate_souffle(call: CallbackQuery):
    img = open('images/DESSERTS/CHOCOLATE SOUFFLE.jpg', 'rb')
    txt = '<b>CHOCOLATE SOUFFLE 9.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=chocolate_souffle_btn)
    await call.message.delete()

#DESSERTS => CHOCOLATE SOUFFLE
@dp.callback_query_handler(text='chocolate_souffle')
async def chocolate_souffle(call: CallbackQuery):
    img = open('images/DESSERTS/CHOCOLATE SOUFFLE.jpg', 'rb')
    txt = '<b>CHOCOLATE SOUFFLE 9.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=chocolate_souffle_btn)
    await call.message.delete()

# DRINKS
@dp.callback_query_handler(text='drinks')
async def drinks(call: CallbackQuery):
    await call.message.answer('<b>DRINKS MENU</b>', parse_mode='html', reply_markup=drinksMenu)
    await call.message.delete()
    await call.answer(cache_time=30)

# DRINKS => MINERALKA 0.5 BG
@dp.callback_query_handler(text='mineralka_0_5bg')
async def mineralka_0_5bg(call: CallbackQuery):
    img = open('images/DRINKS/MINERALKA 0.5L BEZGAZ.jpg', 'rb')
    txt = '<b>MINERALKA 0.5L BEZGAZ 4.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=mineralka_05bg_btn)
    await call.message.delete()

# DRINKS => NEXT MINERALKA 0.5 G
@dp.callback_query_handler(text='next_mineralka_05g_btn')
async def mineralka_0_5g(call: CallbackQuery):
    img = open('images/DRINKS/MINERALKA 0.5L GAZ.jpg', 'rb')
    txt = '<b>MINERALKA 0.5L GAZ 4.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=mineralka_05g_btn)
    await call.message.delete()

# DRINKS => MINERALKA 0.5 G
@dp.callback_query_handler(text='mineralka_0_5g')
async def mineralka_0_5g(call: CallbackQuery):
    img = open('images/DRINKS/MINERALKA 0.5L GAZ.jpg', 'rb')
    txt = '<b>MINERALKA 0.5L GAZ 4.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=mineralka_05g_btn)
    await call.message.delete()

# DRINKS => NEXT MINERALKA 1 BG
@dp.callback_query_handler(text='next_mineralka_1bg_btn')
async def mineralka_1bg(call: CallbackQuery):
    img = open('images/DRINKS/MINERALKA 1L BEZGAZ.jpg', 'rb')
    txt = '<b>MINERALKA 1L BEZGAZ 5.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=mineralka_1bg_btn)
    await call.message.delete()

# DRINKS => MINERALKA 1 BG
@dp.callback_query_handler(text='mineralka_1bg')
async def mineralka_1bg(call: CallbackQuery):
    img = open('images/DRINKS/MINERALKA 1L BEZGAZ.jpg', 'rb')
    txt = '<b>MINERALKA 1L BEZGAZ 5.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=mineralka_1bg_btn)
    await call.message.delete()

# DRINKS => NEXT MINERALKA 1 G
@dp.callback_query_handler(text='next_mineralka_1g_btn')
async def mineralka_1g(call: CallbackQuery):
    img = open('images/DRINKS/MINERALKA 1L GAZ.jpg', 'rb')
    txt = '<b>MINERALKA 1L GAZ 5.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=mineralka_1g_btn)
    await call.message.delete()

# DRINKS => MINERALKA 1 G
@dp.callback_query_handler(text='mineralka_1g')
async def mineralka_1g(call: CallbackQuery):
    img = open('images/DRINKS/MINERALKA 1L GAZ.jpg', 'rb')
    txt = '<b>MINERALKA 1L GAZ 5.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=mineralka_1g_btn)
    await call.message.delete()

# DRINKS => NEXT MINERALKA 1.5 BG
@dp.callback_query_handler(text='next_mineralka_15bg_btn')
async def mineralka_1_5bg(call: CallbackQuery):
    img = open('images/DRINKS/MINERALKA 1.5L BEZGAZ.jpg', 'rb')
    txt = '<b>MINERALKA 1.5L BEZGAZ 6.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=mineralka_15bg_btn)
    await call.message.delete()

# DRINKS => MINERALKA 1.5 BG
@dp.callback_query_handler(text='mineralka_1_5bg')
async def mineralka_1_5bg(call: CallbackQuery):
    img = open('images/DRINKS/MINERALKA 1.5L BEZGAZ.jpg', 'rb')
    txt = '<b>MINERALKA 1.5L BEZGAZ 6.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=mineralka_15bg_btn)
    await call.message.delete()


# DRINKS => NEXT MINERALKA 1.5 G
@dp.callback_query_handler(text='next_mineralka_15g_btn')
async def mineralka_1_5g(call: CallbackQuery):
    img = open('images/DRINKS/MINERALKA 1.5L GAZ.jpg', 'rb')
    txt = '<b>MINERALKA 1.5L GAZ 6.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=mineralka_15g_btn)
    await call.message.delete()

# DRINKS => MINERALKA 1.5 G
@dp.callback_query_handler(text='mineralka_1_5g')
async def mineralka_1_5g(call: CallbackQuery):
    img = open('images/DRINKS/MINERALKA 1.5L GAZ.jpg', 'rb')
    txt = '<b>MINERALKA 1.5L GAZ 6.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=mineralka_15g_btn)
    await call.message.delete()

# DRINKS => NEXT COLA 400
@dp.callback_query_handler(text='next_cola_400_btn')
async def coca_cola_400(call: CallbackQuery):
    img = open('images/DRINKS/COCA COLA 400ML.jpg', 'rb')
    txt = '<b>COCA COLA 400ML 6.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=cola_400_btn)
    await call.message.delete()

# DRINKS => COLA 400
@dp.callback_query_handler(text='coca_cola_400')
async def coca_cola_400(call: CallbackQuery):
    img = open('images/DRINKS/COCA COLA 400ML.jpg', 'rb')
    txt = '<b>COCA COLA 400ML 6.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=cola_400_btn)
    await call.message.delete()

# DRINKS => NEXT COLA 0.5
@dp.callback_query_handler(text='next_cola_05_btn')
async def coca_cola_0_5(call: CallbackQuery):
    img = open('images/DRINKS/COCA COLA 0.5.jpg', 'rb')
    txt = '<b>COCA COLA 0.5L 7.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=cola_05_btn)
    await call.message.delete()

# DRINKS => COLA 0.5
@dp.callback_query_handler(text='coca_cola_0_5')
async def coca_cola_0_5(call: CallbackQuery):
    img = open('images/DRINKS/COCA COLA 0.5.jpg', 'rb')
    txt = '<b>COCA COLA 0.5L 7.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=cola_05_btn)
    await call.message.delete()

# DRINKS => NEXT COLA 1
@dp.callback_query_handler(text='next_cola_1_btn')
async def coca_cola_1(call: CallbackQuery):
    img = open('images/DRINKS/COCA COLA 1L.jpg', 'rb')
    txt = '<b>COCA COLA 1L 11.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=cola_1_btn)
    await call.message.delete()

# DRINKS => COLA 1
@dp.callback_query_handler(text='coca_cola_1')
async def coca_cola_1(call: CallbackQuery):
    img = open('images/DRINKS/COCA COLA 1L.jpg', 'rb')
    txt = '<b>COCA COLA 1L 11.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=cola_1_btn)
    await call.message.delete()

# DRINKS => NEXT COLA 1.5
@dp.callback_query_handler(text='next_cola_15_btn')
async def coca_cola_1_5(call: CallbackQuery):
    img = open('images/DRINKS/COCA COLA 1.5L.jpg', 'rb')
    txt = '<b>COCA COLA 1.5L 14.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=cola_15_btn)
    await call.message.delete()

# DRINKS => COLA 1.5
@dp.callback_query_handler(text='coca_cola_1_5')
async def coca_cola_1_5(call: CallbackQuery):
    img = open('images/DRINKS/COCA COLA 1.5L.jpg', 'rb')
    txt = '<b>COCA COLA 1.5L 14.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=cola_15_btn)
    await call.message.delete()

# DRINKS => NEXT FANTA 400
@dp.callback_query_handler(text='next_fanta_400_btn')
async def fanta_400(call: CallbackQuery):
    img = open('images/DRINKS/FANTA 400ML.jpg', 'rb')
    txt = '<b>FANTA 400ML 6.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=fanta_400_btn)
    await call.message.delete()

# DRINKS => FANTA 400
@dp.callback_query_handler(text='fanta_400')
async def fanta_400(call: CallbackQuery):
    img = open('images/DRINKS/FANTA 400ML.jpg', 'rb')
    txt = '<b>FANTA 400ML 6.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=fanta_400_btn)
    await call.message.delete()

# DRINKS => NEXT FANTA 0.5
@dp.callback_query_handler(text='next_fanta_05_btn')
async def fanta_0_5(call: CallbackQuery):
    img = open('images/DRINKS/FANTA 0.5L.jpg', 'rb')
    txt = '<b>FANTA 0.5L 7.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=fanta_05_btn)
    await call.message.delete()

# DRINKS => FANTA 0.5
@dp.callback_query_handler(text='fanta_0_5')
async def fanta_0_5(call: CallbackQuery):
    img = open('images/DRINKS/FANTA 0.5L.jpg', 'rb')
    txt = '<b>FANTA 0.5L 7.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=fanta_05_btn)
    await call.message.delete()

# DRINKS => NEXT FANTA 1
@dp.callback_query_handler(text='next_fanta_1_btn')
async def fanta_1(call: CallbackQuery):
    img = open('images/DRINKS/FANTA 1L.jpg', 'rb')
    txt = '<b>FANTA 1L 11.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=fanta_1_btn)
    await call.message.delete()

# DRINKS => FANTA 1
@dp.callback_query_handler(text='fanta_1')
async def fanta_1(call: CallbackQuery):
    img = open('images/DRINKS/FANTA 1L.jpg', 'rb')
    txt = '<b>FANTA 1L 11.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=fanta_1_btn)
    await call.message.delete()

# DRINKS => NEXT FANTA 1.5
@dp.callback_query_handler(text='next_fanta_15_btn')
async def fanta_1_5(call: CallbackQuery):
    img = open('images/DRINKS/FANTA 1.5L.jpg', 'rb')
    txt = '<b>FANTA 1.5L 14.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=fanta_15_btn)
    await call.message.delete()

# DRINKS => FANTA 1.5
@dp.callback_query_handler(text='fanta_1_5')
async def fanta_1_5(call: CallbackQuery):
    img = open('images/DRINKS/FANTA 1.5L.jpg', 'rb')
    txt = '<b>FANTA 1.5L 14.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=fanta_15_btn)
    await call.message.delete()

# DRINKS => NEXT SPRITE 400
@dp.callback_query_handler(text='next_sprite_400_btn')
async def sprite_400(call: CallbackQuery):
    img = open('images/DRINKS/SPRITE 400ML.jpg', 'rb')
    txt = '<b>SPRITE 400ML 6.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=sprite_400_btn)
    await call.message.delete()

# DRINKS => SPRITE 400
@dp.callback_query_handler(text='sprite_400')
async def sprite_400(call: CallbackQuery):
    img = open('images/DRINKS/SPRITE 400ML.jpg', 'rb')
    txt = '<b>SPRITE 400ML 6.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=sprite_400_btn)
    await call.message.delete()

# DRINKS => NEXT SPRITE 0.5
@dp.callback_query_handler(text='next_sprite_05_btn')
async def sprite_0_5(call: CallbackQuery):
    img = open('images/DRINKS/SPRITE 0.5L.jpg', 'rb')
    txt = '<b>SPRITE 0.5L 7.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=sprite_05_btn)
    await call.message.delete()

# DRINKS => SPRITE 0.5
@dp.callback_query_handler(text='sprite_0_5')
async def sprite_0_5(call: CallbackQuery):
    img = open('images/DRINKS/SPRITE 0.5L.jpg', 'rb')
    txt = '<b>SPRITE 0.5L 7.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=sprite_05_btn)
    await call.message.delete()

# DRINKS => NEXT SPRITE 1
@dp.callback_query_handler(text='next_sprite_1_btn')
async def sprite_1(call: CallbackQuery):
    img = open('images/DRINKS/SPRITE 1L.jpg', 'rb')
    txt = '<b>SPRITE 1L 11.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=sprite_1_btn)
    await call.message.delete()

# DRINKS => SPRITE 1
@dp.callback_query_handler(text='sprite_1')
async def sprite_1(call: CallbackQuery):
    img = open('images/DRINKS/SPRITE 1L.jpg', 'rb')
    txt = '<b>SPRITE 1L 11.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=sprite_1_btn)
    await call.message.delete()

# DRINKS => NEXT SPRITE 1.5
@dp.callback_query_handler(text='next_sprite_15_btn')
async def sprite_1_5(call: CallbackQuery):
    img = open('images/DRINKS/SPRITE 1.5L.jpg', 'rb')
    txt = '<b>SPRITE 1.5L 14.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=sprite_15_btn)
    await call.message.delete()

# DRINKS => SPRITE 1.5
@dp.callback_query_handler(text='sprite_1_5')
async def sprite_1_5(call: CallbackQuery):
    img = open('images/DRINKS/SPRITE 1.5L.jpg', 'rb')
    txt = '<b>SPRITE 1.5L 14.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=sprite_15_btn)
    await call.message.delete()

# DRINKS => NEXT ICE TEA
@dp.callback_query_handler(text='next_ice_tea_btn')
async def ice_tea(call: CallbackQuery):
    img = open('images/DRINKS/ICE TEA.jpg', 'rb')
    txt = '<b>ICE TEA 11.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=ice_tea_btn)
    await call.message.delete()

# DRINKS => ICE TEA
@dp.callback_query_handler(text='ice_tea')
async def ice_tea(call: CallbackQuery):
    img = open('images/DRINKS/ICE TEA.jpg', 'rb')
    txt = '<b>ICE TEA 11.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=ice_tea_btn)
    await call.message.delete()

# DRINKS => NEXT SOK
@dp.callback_query_handler(text='next_sok_btn')
async def sok_1(call: CallbackQuery):
    img = open('images/DRINKS/SOK 1L.jpg', 'rb')
    txt = '<b>SOK 1L 13.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=sok_btn)
    await call.message.delete()

# DRINKS => SOK
@dp.callback_query_handler(text='sok_1')
async def sok_1(call: CallbackQuery):
    img = open('images/DRINKS/SOK 1L.jpg', 'rb')
    txt = '<b>SOK 1L 13.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=sok_btn)
    await call.message.delete()

# DRINKS => NEXT SOK GRANAT
@dp.callback_query_handler(text='next_sok_granat_btn')
async def sok_1_gr(call: CallbackQuery):
    img = open('images/DRINKS/SOK 1L (GRANAT).jpg', 'rb')
    txt = '<b>SOK 1L (GRANAT) 15.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=sok_granat_btn)
    await call.message.delete()

# DRINKS => SOK GRANAT
@dp.callback_query_handler(text='sok_1_gr')
async def sok_1_gr(call: CallbackQuery):
    img = open('images/DRINKS/SOK 1L (GRANAT).jpg', 'rb')
    txt = '<b>SOK 1L (GRANAT) 15.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=sok_granat_btn)
    await call.message.delete()

# DRINKS => NEXT SOK APELSIN
@dp.callback_query_handler(text='next_sok_apelsin_btn')
async def sok_1_ap(call: CallbackQuery):
    img = open('images/DRINKS/SOK 1L (APELSIN).png', 'rb')
    txt = '<b>SOK 1L (APELSIN) 15.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=sok_apelsin_btn)
    await call.message.delete()

# DRINKS => SOK APELSIN
@dp.callback_query_handler(text='sok_1_ap')
async def sok_1_ap(call: CallbackQuery):
    img = open('images/DRINKS/SOK 1L (APELSIN).png', 'rb')
    txt = '<b>SOK 1L (APELSIN) 15.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=sok_apelsin_btn)
    await call.message.delete()


# KIDS MEAL
@dp.callback_query_handler(text='kids_meal')
async def kids_meal(call: CallbackQuery):
    await call.message.answer('<b>KIDS MEAL MENU</b>', parse_mode='html', reply_markup=kidsMenu)
    await call.message.delete()
    await call.answer(cache_time=30)

# KIDS MEAL => KIDS BURGER
@dp.callback_query_handler(text='kids_burger')
async def kids_burger(call: CallbackQuery):
    img = open('images/KIDS MEAL/KIDS BURGER.jpg', 'rb')
    txt = '<b>KIDS BURGER 13.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=kids_burger_btn)
    await call.message.delete()

# KIDS MEAL => NEXT KIDS SPINNER
@dp.callback_query_handler(text='next_kids_spinner_btn')
async def kids_spinner(call: CallbackQuery):
    img = open('images/KIDS MEAL/KIDS SPINNER.jpg', 'rb')
    txt = '<b>KIDS SPINNER 10.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=kids_spinner_btn)
    await call.message.delete()

# KIDS MEAL => KIDS SPINNER
@dp.callback_query_handler(text='kids_spinner')
async def kids_spinner(call: CallbackQuery):
    img = open('images/KIDS MEAL/KIDS SPINNER.jpg', 'rb')
    txt = '<b>KIDS SPINNER 10.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=kids_spinner_btn)
    await call.message.delete()

# KIDS MEAL => NEXT KIDS MENU STRIPS BOY
@dp.callback_query_handler(text='next_kids_menu_strips_boy_btn')
async def kids_strips_boy(call: CallbackQuery):
    img = open('images/KIDS MEAL/KIDS MENU STRIPS BOY.jpg', 'rb')
    txt = '<b>KIDS MENU STRIPS BOY 33.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=kids_menu_strips_boy_btn)
    await call.message.delete()

# KIDS MEAL => KIDS MENU STRIPS BOY
@dp.callback_query_handler(text='kids_strips_boy')
async def kids_strips_boy(call: CallbackQuery):
    img = open('images/KIDS MEAL/KIDS MENU STRIPS BOY.jpg', 'rb')
    txt = '<b>KIDS MENU STRIPS BOY 33.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=kids_menu_strips_boy_btn)
    await call.message.delete()

# KIDS MEAL => NEXT KIDS MENU STRIPS GIRL
@dp.callback_query_handler(text='next_kids_menu_strips_girl_btn')
async def kids_strips_girl(call: CallbackQuery):
    img = open('images/KIDS MEAL/KIDS MENU STRIPS GIRL.jpg', 'rb')
    txt = '<b>KIDS MENU STRIPS GIRL 33.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=kids_menu_strips_girl_btn)
    await call.message.delete()

# KIDS MEAL => KIDS MENU STRIPS GIRL
@dp.callback_query_handler(text='kids_strips_girl')
async def kids_strips_girl(call: CallbackQuery):
    img = open('images/KIDS MEAL/KIDS MENU STRIPS GIRL.jpg', 'rb')
    txt = '<b>KIDS MENU STRIPS GIRL 33.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=kids_menu_strips_girl_btn)
    await call.message.delete()

# KIDS MEAL => NEXT KIDS MENU SPINNER BOY
@dp.callback_query_handler(text='next_kids_menu_spinner_boy_btn')
async def kids_spinner_boy(call: CallbackQuery):
    img = open('images/KIDS MEAL/KIDS MENU SPINNER BOY.jpg', 'rb')
    txt = '<b>KIDS MENU SPINNER BOY 33.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=kids_menu_spinner_boy_btn)
    await call.message.delete()

# KIDS MEAL => KIDS MENU SPINNER BOY
@dp.callback_query_handler(text='kids_spinner_boy')
async def kids_spinner_boy(call: CallbackQuery):
    img = open('images/KIDS MEAL/KIDS MENU SPINNER BOY.jpg', 'rb')
    txt = '<b>KIDS MENU SPINNER BOY 33.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=kids_menu_spinner_boy_btn)
    await call.message.delete()

# KIDS MEAL => NEXT KIDS MENU SPINNER GIRL
@dp.callback_query_handler(text='next_kids_menu_spinner_girl_btn')
async def kids_spinner_girl(call: CallbackQuery):
    img = open('images/KIDS MEAL/KIDS MENU SPINNER GIRL.jpg', 'rb')
    txt = '<b>KIDS MENU SPINNER GIRL 33.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=kids_menu_spinner_girl_btn)
    await call.message.delete()

# KIDS MEAL => KIDS MENU SPINNER GIRL
@dp.callback_query_handler(text='kids_spinner_girl')
async def kids_spinner_girl(call: CallbackQuery):
    img = open('images/KIDS MEAL/KIDS MENU SPINNER GIRL.jpg', 'rb')
    txt = '<b>KIDS MENU SPINNER GIRL 33.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=kids_menu_spinner_girl_btn)
    await call.message.delete()


# COMBO
@dp.callback_query_handler(text='combo')
async def combo(call: CallbackQuery):
    await call.message.answer('<b>COMBO MENU</b>', parse_mode='html', reply_markup=comboMenu)
    await call.message.delete()
    await call.answer(cache_time=30)

# COMBO => COMBO
@dp.callback_query_handler(text='combo_')
async def combo_(call: CallbackQuery):
    img = open('images/COMBO/COMBO.jpg', 'rb')
    txt = '<b>COMBO 13.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=combo_btn)
    await call.message.delete()

# COMBO => NEXT WICKED COMBO STRIPS
@dp.callback_query_handler(text='next_wicked_combo_strips_btn')
async def wicked_combo_strips(call: CallbackQuery):
    img = open('images/COMBO/WICKED COMBO (strips).jpg', 'rb')
    txt = '<b>WICKED COMBO (strips) 22.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=wicked_combo_strips_btn)
    await call.message.delete()

# COMBO => WICKED COMBO STRIPS
@dp.callback_query_handler(text='wicked_combo_strips')
async def wicked_combo_strips(call: CallbackQuery):
    img = open('images/COMBO/WICKED COMBO (strips).jpg', 'rb')
    txt = '<b>WICKED COMBO (strips) 22.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=wicked_combo_strips_btn)
    await call.message.delete()

# COMBO => NEXT WICKED COMBO WINGS
@dp.callback_query_handler(text='next_wicked_combo_wings_btn')
async def wicked_combo_wings(call: CallbackQuery):
    img = open('images/COMBO/WICKED COMBO (wings).jpg', 'rb')
    txt = '<b>WICKED COMBO (wings) 22.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=wicked_combo_wings_btn)
    await call.message.delete()

# COMBO => WICKED COMBO WINGS
@dp.callback_query_handler(text='wicked_combo_wings')
async def wicked_combo_wings(call: CallbackQuery):
    img = open('images/COMBO/WICKED COMBO (wings).jpg', 'rb')
    txt = '<b>WICKED COMBO (wings) 22.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=wicked_combo_wings_btn)
    await call.message.delete()

# COMBO => NEXT FULLY COMBO NORMAL
@dp.callback_query_handler(text='next_fully_combo_normal_btn')
async def fully_combo_normal(call: CallbackQuery):
    img = open('images/COMBO/FULLY COMBO (normal).jpg', 'rb')
    txt = '<b>FULLY COMBO (normal) 22.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=fully_combo_normal_btn)
    await call.message.delete()

# COMBO => FULLY COMBO NORMAL
@dp.callback_query_handler(text='fully_combo_normal')
async def fully_combo_normal(call: CallbackQuery):
    img = open('images/COMBO/FULLY COMBO (normal).jpg', 'rb')
    txt = '<b>FULLY COMBO (normal) 22.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=fully_combo_normal_btn)
    await call.message.delete()

# COMBO => NEXT FULLY COMBO SPICY
@dp.callback_query_handler(text='next_fully_combo_spicy_btn')
async def fully_combo_spicy(call: CallbackQuery):
    img = open('images/COMBO/FULLY COMBO (spicy).jpg', 'rb')
    txt = '<b>FULLY COMBO (spicy) 22.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=fully_combo_spicy_btn)
    await call.message.delete()

# COMBO => FULLY COMBO SPICY
@dp.callback_query_handler(text='fully_combo_spicy')
async def fully_combo_spicy(call: CallbackQuery):
    img = open('images/COMBO/FULLY COMBO (spicy).jpg', 'rb')
    txt = '<b>FULLY COMBO (spicy) 22.000 UZS</b>'
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=fully_combo_spicy_btn)
    await call.message.delete()

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
