#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
author: Smoke_87
e-mail: sergmadox@yandex.ru
"""
import time
import telepot
import const.const as const
import function.function as function
import function.feed_parser as feed_parser
from telepot.namedtuple import *
# Прописываем Token
bot = telepot.Bot(const.token)

def news_in_group(feed,from_id):
    news = feed_parser.get_news_from_bankir(feed)
    for i in news:
        bot.sendMessage(from_id, i)

def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    Inline_keyboard = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text='bankir.ru', callback_data='bankir')],
        [InlineKeyboardButton(text='rg.ru', callback_data='rg')],
        [InlineKeyboardButton(text='fontanka.ru', callback_data='fontanka')],
        [InlineKeyboardButton(text='blackmoreops.com', callback_data='blackmoreops')],
        [InlineKeyboardButton(text='okbank.ru', callback_data='okbank')]
    ])

    print(content_type, chat_type, chat_id)

    if content_type == 'text':
        is_command = bot.getUpdates()
        person = is_command[0]['message']['from']['first_name']
        if (is_command[0]['message']['text'] == '/start') or (is_command[0]['message']['text'] == '/start@OK_bank_bot'):
            bot.sendMessage(chat_id,function.reply_time_now(const.time_now) + person + function.start())
        elif (is_command[0]['message']['text'] == '/help') or (is_command[0]['message']['text'] == '/help@OK_bank_bot'):
            bot.sendMessage(chat_id,function.help())
        elif (is_command[0]['message']['text'] == '/memory') or (is_command[0]['message']['text'] == '/memory@OK_bank_bot'):
            bot.sendMessage(chat_id,function.memory())
        elif (is_command[0]['message']['text'] == '/weather') or (is_command[0]['message']['text'] == '/weather@OK_bank_bot'):
            bot.sendMessage(chat_id, function.weather())
        elif (is_command[0]['message']['text'] == '/kurs') or (is_command[0]['message']['text'] == '/kurs@OK_bank_bot'):
            bot.sendMessage(chat_id, function.kurs())
        elif (is_command[0]['message']['text'] == '/news') or (is_command[0]['message']['text'] == '/news@OK_bank_bot'):
            bot.sendMessage(chat_id,'Выбрете новостной сайт',reply_markup=Inline_keyboard)

def on_callback_query(msg):
    query_id, from_id, query_data = telepot.glance(msg, flavor='callback_query')
    print('Callback Query:', query_id, from_id, query_data)
    bot.answerCallbackQuery(query_id, text='Пробую найти новости')
    print(from_id)
    dict = {'bankir':'http://bankir.ru/rss/news','rg':'https://rg.ru/tema/ekonomika/rss.xml',
            'fontanka':'http://www.fontanka.ru/fontanka.rss','blackmoreops':'https://www.blackmoreops.com/feed/',
            'okbank':'http://www.okbank.ru/news/rss.xml'}
    news_in_group(dict[query_data],from_id)


bot.message_loop({'chat': handle,
                  'callback_query': on_callback_query})
print ('Listening ...')

# Вечный цикл программы
while True:
    time.sleep(10)