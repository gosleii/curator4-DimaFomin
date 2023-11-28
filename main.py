import telebot
import random
from telebot import types

bot = telebot.TeleBot('6306321709:AAH_CAjBjw4MVx_kGg3ioXyaV5sWRp7JcrU')

@bot.message_handler(commands=['start'])
def lalala(message):
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("ПОЛУЧИТЬ АНЕКДОТ")
    item2 = types.KeyboardButton("ПОЛУЧИТЬ РАНДОМНОЕ ЧИСЛО")

    markup.add(item1, item2)

    bot.send_message(message.chat.id,'Привет {0.first_name}! Я твой первый бот, чтобы начать пользоваться ботом, нажимай кнопки ниже'.format(message.from_user, bot.get_me()), parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'ПОЛУЧИТЬ РАНДОМНОЕ ЧИСЛО':
            bot.send_message(message.chat.id, str(random.randint(0,1000)))
        elif message.text == 'ПОЛУЧИТЬ АНЕКДОТ':

            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("ДА, Я ЗАУЛЫБАЛСЯ", callback_data='WRITE A JOKE')
            item2 = types.InlineKeyboardButton("НЕТ, АНЕКДОТ НЕ СМЕШНОЙ", callback_data='REFUSE')

            markup.add(item1, item2)

            bot.send_message(message.chat.id, 'Сын говорит отцу: — Папа я женюсь\n Отец: — На ком?\n Сын: - На Иване из 5 подъезда\n Отец: — Так он же пацан\n Сын: - Нифига себе пацан, 38 лет')
            bot.send_message(message.chat.id, 'Поднял ли я тебе настроение?', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить')

@bot.callback_query_handler(func=lambda call: True)
def keyboard(call):
    try:
        if call.message:
            if call.data == 'WRITE A JOKE':
                bot.send_message(call.message.chat.id, 'Отлично, я рад за тебя!')
            elif call.data == 'REFUSE':
                bot.send_message(call.message.chat.id, 'Эхх... Надеюсь в следующий раз у меня получится тебя расмешить')

    except Exception as e:
        print(repr(e))

bot.polling(none_stop=True)