import telebot
import config
import random
import threading
from spamm import spamm
from telebot import types
 

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message): 
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Что я такое")
    item2 = types.KeyboardButton("Спонсорство")
 
    markup.add(item1, item2)
    bot.send_message(message.chat.id,
                     "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы быть спамить на номера телефона, все что нужно, отпраить мне код страны и номер телефона через пробел".format(
                         message.from_user, bot.get_me()))


@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Что я такое':
            bot.send_message(message.chat.id,
                             "Дорогой друг, я бот который предназачен для Спама смс на определенный номер, все что нужно, отправить мне код страны и номер телефона одним сообщением через пробел")
        elif message.text == 'Спонсорство':
            bot.send_message(message.chat.id,
                             "Дорогой друг! Увы, но мне нужны деньги, деньги на аренду VDS, если хочешь мне помочь, пиши сюда №№№№№№")
        else:
            try:
                data = message.text.split()
                data_user = message.from_user
                if len(data) >= 3:
                    bot.send_message(message.chat.id, 'Я не понимаю((')
                    return
                if len(data) <= 1:
                    bot.send_message(message.chat.id, 'Я не понимаю((')
                    return
                _phone = data[0] + data[1]
                print(_phone)
                for lett in _phone:
                    if lett not in '1234567890+':
                        bot.send_message(message.chat.id, 'Я не понимаю((')
                        return

                bot.send_message(message.chat.id,
                                 'Начинаю спамить на номер {1} с кодом страны {0}'.format(data[0], data[1]))
                t = threading.Thread(target=spamm, name='threading{}'.format(message.chat.id),
                                     args=(data[1], data[0], message.chat.id, bot))

                with open('loggin.txt', 'a') as f:
                    f.write(data_user.username + ' ' + data_user.first_name + ' ' + str(data_user.last_name) + ' ' + data[1] + ' ' + data[0] + '\n')
                t.start()
            except:
                bot.send_message(message.chat.id, 'Я не понимаю((')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Я бот который спамит сообщения, что бы начать спамить, введи номер и код страны через пробел')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Реквизиты для спонсорства: QIWI №№№№№  VTB №№№№№№№№№№')
    except Exception as e:
        print(repr(e))



try:
     bot.polling(none_stop=True)
except:
    print('Ошибка, либо рип впн(РКН заебал блокировать все и вся), либо токен не верный или отсутсвует, либо отсутствует соеденение')