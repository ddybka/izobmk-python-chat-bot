import random
import telebot
import tokenbot
from anecdotes import *
from telebot import types

bot = telebot.TeleBot(tokenbot.TOKEN)
print("Начало работы бота...")

def get_meme_name():
    num = random.randint(1, 5)
    return f"media/meme_{num}.jpg"

def get_anecdote():
    num = random.randint(0, len(ANECDOTES) - 1)
    return ANECDOTES[num]

##
## COMMANDS
##

@bot.message_handler(commands=['start'])
def start(m):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    sendAnekgot = types.KeyboardButton('Рассказать анекдот')
    sendMemes = types.KeyboardButton('Отправить мемчик')
    writeToAdmin = types.KeyboardButton('/help')
    markup.row(sendAnekgot, sendMemes).add(writeToAdmin)

    bot.send_message(m.chat.id, 'Привет, это Telegram чат-бот из мастер-класса «Изобретариума», который мы будем программировать с детьми.', reply_markup=markup)

@bot.message_handler(commands=['help'])
def help(m):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Официальный сайт", url="https://izobretarium.ru"))
    markup.add(types.InlineKeyboardButton("Ссылка на исходник", url="https://github.com/ddybka/izobmk-python-chat-bot"))
    markup.add(types.InlineKeyboardButton("Связаться с автором", url="https://ddybka.t.me"))

    bot.send_message(m.chat.id, "Ну мы тут делаем своего чат-бота, пользуйтесь!", reply_markup=markup)

# ##
# ## TEXT
# ##

@bot.message_handler(content_types=['text'])
def send_text(m):
    text = m.text.lower()
    if text == "рассказать анекдот":
        bot.send_message(m.chat.id, get_anecdote())
    elif text == "отправить мемчик":
        meme = [types.InputMediaPhoto(open(get_meme_name(), 'rb'))]
        bot.send_media_group(m.chat.id, meme)

##
## RUN
##

if __name__ == "__main__":
    bot.polling(none_stop=True)

print("Завершение работы бота...")
