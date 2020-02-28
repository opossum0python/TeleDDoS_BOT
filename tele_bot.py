import telebot
import config
import random
import threading
from spamm import spamm

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
                         message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=markup)


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
                if len(data) >= 3:
                    bot.send_message(message.chat.id, 'Я не понимаю((')
                    return
                if len(data) <= 1:
                    bot.send_message(message.chat.id, 'Я не понимаю((')
                    return
                _phone = data[0] + data[1]
                for lett in _phone:
                    if lett not in '1234567890+':
                        bot.send_message(message.chat.id, 'Я не понимаю((')
                        return

                bot.send_message(message.chat.id,
                                 'Начинаю спамить на номер {1} с кодом страны {0}'.format(data[0], data[1]))
                t = threading.Thread(target=spamm, name='threading{}'.format(message.chat.id), args=(data[1], data[0], message.chat.id, bot))
                t.start()
            except:
                bot.send_message(message.chat.id, 'Я не понимаю((')


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id,
                                 'Я бот который спамит сообщения, что бы начать спамить, введи номер и код страны через пробел')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Реквизиты для спонсорства: QIWI №№№№№  VTB №№№№№№№№№№')
    except Exception as e:
        print(repr(e))


while True:
    try:
        bot.polling(none_stop=True)
    except:
        print('Ошибка, либо рип впн(РКН заебал блокировать все и вся), либо токен не верный или отсутсвует, либо отсутствует соеденение')
