import telebot
from config import API_TOKEN

from telebot.types import (KeyboardButton,
                    ReplyKeyboardMarkup,
                    ReplyKeyboardRemove,
                    Message)


keyboard = ReplyKeyboardMarkup ()
button = KeyboardButton (text="Моя кнопка")
button2 = KeyboardButton(text="Точно моя кнопка")
# button3 = KeyboardButton(text="Прям точно моя кнопка")
keyboard.add(button)
keyboard.add(button2)
keyboard.add("1","2")
# keyboard.row("5","6","7")

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message:Message):
    bot.reply_to(message, f"Привет!, {message.from_user.first_name}")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message: Message):
    bot.reply_to(message, message.text)


bot.infinity_polling()