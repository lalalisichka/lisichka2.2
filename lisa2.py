#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

import telebot
from config import API_TOKEN
from telebot.types import (KeyboardButton, ReplyKeyboardMarkup,ReplyKeyboardRemove,Message)

API_TOKEN = '<api_token>'
keyboard = ReplyKeyboardMarkup()
button = KeyboardButton(text = 'Налево', request_location=True)
button2 = KeyboardButton (text = 'Направо')
# button3 = KeyboardButton (text = 'Моя кнопка 3')
keyboard.add(button)
keyboard.add(button2)
keyboard.add('1', '2')
bot = telebot.TeleBot(API_TOKEN)
state = tuple()
state = 0


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message: Message):
    global state
    hello_message =  f'Привет, <b>{message.from_user.first_name}</b>!!!'
    bot.send_message(
        message.chat.id,
        hello_message,
        reply_markup=keyboard,
          parse_mode= 'HTML'
    )
    state[message.from_user.id] = 1
    print(state)
    
@bot.message_handler(func=lambda message: True)
def text_message(message: Message):
    global state
    if state == 1 and message.text == 'Налево':
        bot.send_message(
            message.chat.id,
            'Вы пошли налево во вторую комнату'
        )
        state = 2
    elif state == 1 and message_text == 'Направо':
        bot.send_message(
            message.chat.id,
            'Вы пошли направо в третью комнату'
        )
        state = 3
elif message.text == "Налево" and state == 2:
    bot.send_message(
        message.from_user.id,
        'Ты в комнате 4. Пути дальше нет.',
  )
    state = 0

elif message.text == "Направо" and state == 2:
    bot.send_message(
        message.from_user.id,
        'Ты в комнате 5. Пути дальше нет.',
    )
    state = 0

elif message.text == "Налево" and state == 3:
    bot.send_message(
        message.from_user.id,
        'Пути дальше нет.',
    )
    state = 0

elif message.text == "Направо" and state == 3:
    bot.send_message(
        message.from_user.id,
        'Пути дальше нет.',
    )
    state = 0

else:
    bot.send_message(
        message.from_user.id,
        'Не туда'
    )
bot.infinity_polling()





