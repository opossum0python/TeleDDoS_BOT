# TeleDDoS_BOT

Привет 
Данный бот спамит смс на введенный номер
Мой бот работает через телеграмм
Для корректной работы бота необходим Python3.7 а так же следующие модули telebot requests прописав в командной строке\термиале следующие команды 'pip install pytelegrambotapi==3.6.7'; 'pip install requests'
Для того что бы создать бота в телеграмме потребуется написать @BotFather и действовать по инструкции, после чего взять токен и вставить в файл config.py
Бот работает с украискими, белорусскими и российскими номерами 
в файле spamm.py написаны запросы для отправки смс, многие из них устарели, можно переписать(в блоке try сменить ссыль и\или поменять запрос)
запуск бота происходит через запуск файла tele_bot.pyл
для изменения колличества циклов атаки изменить зачение number_of_cycles в файле config
