#!/usr/bin/python
#-*- coding: utf-8 -*-
import const.const as const
import requests
def reply_time_now(time):
    time_now = time.split('-')
    if time_now[0] in range(13):
        message = 'Доброе утро, '
    elif time_now[0] in range(13,18,1):
        message = 'Добрый день, '
    else:
        message = 'Добрый вечер, '
    return message


def start():
    message = """
Я - бот Банка АО "Объединенный капитал".
Меня зовут Банковский консультант. Мои команды
вы можете найти в панели команд и воспользоваться
ими в удобный для вас момент.

Бот создан для информирования сотрудников

Если у вас возникнут предложения по расширению моего
функционала, то вы можете отправить свои предложения
администратору чата."""
    return message

def help():
    message = """/news - Последние новости с разных каналов;
/kurs - Курс евро и доллара выставленных на сайте ЦБ;
/weather - Температура воздуха за окном;
/memory - Техническая информация по серверу;
/start - Начало работы со мной;
/help - Помощь.
    """
    return message

def memory():
    import subprocess as sub
    p = sub.Popen(['free', '-t', '-m'],stdout=sub.PIPE,stderr=sub.PIPE)
    output, errors = p.communicate()
    return output

def weather():
    url_weather = 'http://api.openweathermap.org/data/2.5/weather?q=NovayaGollandiya,ru&units=metric&lang=Ru&appid= HERE----YOUR------TOKEN '
    res = requests.get(url_weather)
    current_weather = res.json()
    current = current_weather['weather'][0]['description']
    emojii = const.SHINE +  const.CLOUDY
    wind = str(current_weather['wind']['speed'])
    weather = 'Температура воздуха: ' + str(current_weather['main']['temp']) + ' C '+ '\n\n' + 'Возможный максимум: ' + str(current_weather['main']['temp_max']) + ' C \n'\
              'Возможный минимум: ' + str(current_weather['main']['temp_min']) + \
              ' C ' +'\n\n' + emojii + current + emojii[::-1] + '\n\n' + \
              (const.WIND) + '  ' + ' ветер: ' + wind + ' м/c' + '   ' + (const.WIND)
    return weather

def kurs():
    url_kurs = 'http://www.cbr-xml-daily.ru/daily_json.js'
    kurs = requests.get(url_kurs)
    current_kurs = kurs.json()
    date = str(current_kurs['Date'])
    DOLL = str(current_kurs['Valute']['USD']['Value'])
    EUR = str(current_kurs['Valute']['EUR']['Value'])
    result = 'На '+ date[:10]  + ':\n' +\
             'Курс ' + const.US + ' = ' + DOLL + ' руб. \n' + 'Курс ' + const.EU + ' = ' + EUR +' руб.'
    return result
