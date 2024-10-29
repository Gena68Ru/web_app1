import telebot
import requests
from telebot import types


TOKEN = '7567621533:AAFGo1BIvOwpdBLX60_E4_qIkAqiEXc3f2E'
bot = telebot.TeleBot (TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    markup=types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1=types.KeyboardButton('Зафиксировать нарушение.')
    btn2=types.KeyboardButton('🤝 Нарушения переданные мной.')

    markup.add(btn1,btn2)
    bot.send_message(message.chat.id,'Добро пожаловать в наш телеграмм бот!'+message.from_user.first_name,reply_markup=markup)

@bot.message_handler(commands=['btn1'])
def naruhenie(message):
    first_name = input('Представьтесь пожалуйста: /n Фамилия:')



bot.polling(none_stop=True)
