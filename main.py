from aiogram import executor
from aiogram.types import *
from button_menu import chooseMenu, orderMenu
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
    await msg.answer('<b>Assalom aleykum!</b>\n<b><i>"LOOOK"</i></b> '
                    'buyurtma botiga hush kelibsiz!\n', parse_mode='html', reply_markup=orderMenu)

# MENU
@dp.callback_query_handler(text='order')
async def to_menu(call: CallbackQuery):
    await call.message.edit_text('<b>Tanlang!</b>', parse_mode='html', reply_markup=chooseMenu)


# BACK TO MENU
@dp.callback_query_handler(text='back_to_menu')
async def to_menu(call: CallbackQuery):
    await call.message.edit_text('<b>Tanlang!</b>', parse_mode='html',reply_markup=chooseMenu)

# BACK
@dp.callback_query_handler(text='back')
async def back(call: CallbackQuery):
    await call.message.edit_reply_markup(reply_markup=appetizersMenu)

# # NEXT
# @dp.callback_query_handler(text='next')
# async def back(call: CallbackQuery):
#     await call.message.edit_reply_markup(reply_markup=appetizersMenu)
#     await call.message.delete()

# CANCEL
@dp.callback_query_handler(text='cancel')
async def cancel(call: CallbackQuery):
    await call.message.edit_text('<b>Assalom aleykum!</b>\n<b><i>"LOOOK"</i></b> '
                    'buyurtma botiga hush kelibsiz!\n', parse_mode='html',reply_markup=orderMenu)


# APPETIZERS
@dp.callback_query_handler(text='appetizers')
async def appetizers(call: CallbackQuery):
    await call.message.edit_text('<b>Buyurtma qiling!</b>', parse_mode='html', reply_markup=appetizersMenu)


@dp.callback_query_handler(text='fries')
async def fries(call: CallbackQuery):
    txt = '<b>11000 UZS</b>'
    img = open('menu images/appetizers/fries.jpg', 'rb')
    await call.message.answer_photo(img, caption=txt, parse_mode='html', reply_markup=fries_btn)
    # await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)
    await call.message.delete()

@dp.callback_query_handler(text='strips1')
async def strips1(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='cheese_fries')
async def cheese_fries(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='strips3')
async def strips3(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='rustic_fries')
async def rustic_fries(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='strips5')
async def strips5(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='bites')
async def bites(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='strips7')
async def strips7(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='friends')
async def friends(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='wings1')
async def wings1(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='mushrooms')
async def mushrooms(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='hot_wings3')
async def hot_wings3(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='teriyaki_wings3')
async def teriyaki_wings3(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='hot_wings5')
async def hot_wings5(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='cheese_nuggets')
async def cheese_nuggets(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='hot_wings7')
async def hot_wings7(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='chechevit_soup')
async def chechevit_soup(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)




# BURGERS
@dp.callback_query_handler(text='burgers')
async def burgers(call: CallbackQuery):
    await call.message.edit_text('<b>Buyurtma qiling!</b>', parse_mode='html', reply_markup=burgersMenu)

@dp.callback_query_handler(text='classic')
async def classic(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='junior_burger')
async def junior_burger(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='longer')
async def longer(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='hamburger')
async def hamburger(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='bigger')
async def bigger(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='cheese_burger')
async def cheese_burger(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='chili_longer')
async def chili_longer(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='barbecue_burger')
async def barbecue_burger(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='beef_longer')
async def beef_longer(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='chicky_burger')
async def chicky_burger(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='cheesy_burger')
async def cheesy_burger(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='roast_burger')
async def roast_burger(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='double_cheese_longer')
async def double_cheese_longer(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)




# PIZZA
@dp.callback_query_handler(text='pizza')
async def pizza(call: CallbackQuery):
    await call.message.edit_text('<b>Buyurtma qiling!</b>', parse_mode='html', reply_markup=pizzaMenu)

@dp.callback_query_handler(text='pizza_supreme')
async def pizza_supreme(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='pizza_steak')
async def pizza_steak(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='pizza_spicy')
async def pizza_spicy(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='pizza_bbq_chicken')
async def pizza_bbq_chicken(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='pizza_vegetarian')
async def pizza_vegetarian(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='pizza_white_cheese')
async def pizza_white_cheese(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='pizza_hawaiian')
async def pizza_hawaiian(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='pizza_pepperoni')
async def pizza_pepperoni(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='pizza_margarita')
async def pizza_margarita(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='pizza_frankfurt')
async def pizza_frankfurt(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)




# SPINNER
@dp.callback_query_handler(text='spinner')
async def spinner(call: CallbackQuery):
    await call.message.edit_text('<b>Buyurtma qiling!</b>', parse_mode='html', reply_markup=spinnerMenu)

@dp.callback_query_handler(text='spinner_snack')
async def spinner_snack(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='spinner_salsa')
async def spinner_salsa(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='spinner_tako')
async def spinner_tako(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='spinner_no_souce')
async def spinner_no_souce(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='duet_master')
async def duet_master(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='smile_box')
async def smile_box(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='spinner_super_charged')
async def spinner_super_charged(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)



# CHICKEN
@dp.callback_query_handler(text='chicken')
async def chicken(call: CallbackQuery):
    await call.message.edit_text('<b>Buyurtma qiling!</b>', parse_mode='html', reply_markup=chickenMenu)

@dp.callback_query_handler(text='chicken1_spicy')
async def chicken1_spicy(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='chicken1_normal')
async def chicken1_normal(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='snack_meal_spicy')
async def snack_meal_spicy(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='snack_meal_normal')
async def snack_meal_normal(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='dinner_meal_normal')
async def dinner_meal_normal(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='dinner_meal_spicy')
async def dinner_meal_spicy(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='mix_meal_normal')
async def mix_meal_normal(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='double_meal')
async def double_meal(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='chicken12_set_normal')
async def chicken12_set_normal(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='chicken12_set_spicy')
async def chicken12_set_spicy(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)



# SALADS AND OTHER
@dp.callback_query_handler(text='salads')
async def salads(call: CallbackQuery):
    await call.message.edit_text('<b>Buyurtma qiling!</b>', parse_mode='html', reply_markup=saladMenu)

@dp.callback_query_handler(text='coleslaw_salad')
async def coleslaw_salad(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='loook_salad')
async def loook_salad(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='veggie_fresh_salad')
async def veggie_fresh_salad(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='bread_pikelet')
async def bread_pikelet(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)



# DESSERTS
@dp.callback_query_handler(text='desserts')
async def desserts(call: CallbackQuery):
    await call.message.edit_text('<b>Buyurtma qiling!</b>', parse_mode='html', reply_markup=dessertMenu)

@dp.callback_query_handler(text='red_wave')
async def red_wave(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='lemon_cake')
async def lemon_cake(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='kiwix')
async def kiwix(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='chocotastic')
async def chocotastic(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='tello')
async def tello(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='sugar_chip')
async def sugar_chip(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='chocolate_souffle')
async def chocolate_souffle(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)



# DRINKS
@dp.callback_query_handler(text='drinks')
async def drinks(call: CallbackQuery):
    await call.message.edit_text('<b>Buyurtma qiling!</b>', parse_mode='html', reply_markup=drinksMenu)

@dp.callback_query_handler(text='mineralka_0_5bg')
async def mineralka_0_5bg(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='fanta_0_5')
async def fanta_0_5(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='mineralka_0_5g')
async def mineralka_0_5g(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='fanta_1')
async def fanta_1(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='mineralka_1bg')
async def mineralka_1bg(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='fanta_1_5')
async def fanta_1_5(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='mineralka_1g')
async def mineralka_1g(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='sprite_400')
async def sprite_400(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='mineralka_1_5bg')
async def mineralka_1_5bg(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='sprite_0_5')
async def sprite_0_5(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='mineralka_1_5g')
async def mineralka_1_5g(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='sprite_1')
async def sprite_1(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='coca_cola_400')
async def coca_cola_400(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='sprite_1_5')
async def sprite_1_5(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='coca_cola_0_5')
async def coca_cola_0_5(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='ice_tea')
async def ice_tea(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='coca_cola_1')
async def coca_cola_1(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='sok_1')
async def sok_1(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='coca_cola_1_5')
async def coca_cola_1_5(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='sok_1_gr')
async def sok_1_gr(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='fanta_400')
async def fanta_400(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='sok_1_ap')
async def sok_1_ap(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)



# KIDS MEAL
@dp.callback_query_handler(text='kids_meal')
async def kids_meal(call: CallbackQuery):
    await call.message.edit_text('<b>Buyurtma qiling!</b>', parse_mode='html', reply_markup=kidsMenu)

@dp.callback_query_handler(text='kids_burger')
async def kids_burger(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='kids_spinner')
async def kids_spinner(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='kids_strips_boy')
async def kids_strips_boy(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='kids_strips_girl')
async def kids_strips_girl(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='kids_spinner_boy')
async def kids_spinner_boy(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='kids_spinner_girl')
async def kids_spinner_girl(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)



# COMBO
@dp.callback_query_handler(text='combo')
async def combo(call: CallbackQuery):
    await call.message.edit_text('<b>Buyurtma qiling!</b>', parse_mode='html', reply_markup=comboMenu)

@dp.callback_query_handler(text='combo_')
async def combo_(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='wicked_combo_strips')
async def wicked_combo_strips(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='wicked_combo_wings')
async def wicked_combo_wings(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='fully_combo_normal')
async def fully_combo_normal(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)

@dp.callback_query_handler(text='fully_combo_spicy')
async def fully_combo_spicy(call: CallbackQuery):
    await call.answer('Qabul qilindi!', cache_time=30, show_alert=True)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
