import requests
import telebot
import json
from config import keys, TOKEN
from utills import ConvertionExeption, ValutConvertion

bot = telebot.TeleBot (TOKEN)
@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text= 'Чтобы начать работу введите боту команду в следующем формате:\n<имя валюты>\
<в какую валюту перевести\
<количество переводимой валюты>.\nУвидеть все доступные валюты:/values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values']) # список доступных валют
def values(message: telebot.types.Message):
    text= 'Доступные валюты:'
    for key in keys.keys():
        text= '\n'.join((text, key))
    bot.reply_to(message, text)

@bot.message_handler(content_types=['text', ])# основной обработчик
def convert(message: telebot.types.Message):
    try:
        values=message.text.split(' ')
        if len(values)!=3:
            raise ConvertionExeption('Много параметров')

        quote, base, amount = values
        total_base= ValutConvertion.covert(quote, base, amount)
    except ConvertionExeption as e:
        bot.reply_to(message,f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message,f'Не удалось обработать команду.\n{e}')
    else:
        text=f'Цена {amount} {quote} в {base} - {total_base}'
    bot.send_message(message.chat.id, text)


bot.polling()
