import random
import telebot
import tokenbot
from anecdotes import *
from telebot import types

##
## Для запуска бота:
##
## 1. Terminal (Терминал) > New Terminal (Новый терминал)
## (в самом верху слева)
## 2. Вы должны находиться в папке src, для перемещения используйте:
##   - cd ..     - перейти выше
##   - cd folder - перейти в папку folder
## 3. Введите команду python main.py (либо python3 main.py)
## 4. После изменений в боте остановите бота (Ctrl + C / Cmd + C) и повторите 3 пункт
##

bot = telebot.TeleBot(tokenbot.TOKEN)
print("Начало работы бота...")

##
## Загрузить новый мем:
##
## 1. Скачайте мем из интернета
## 2. Переименуйте его в "meme_<number>.jpg", где <number> - следующий номер мема
## (после 5 идет 6 номер, после 6 идет 7 номер..)
## 3. Загрузите в media
## 4. Поменяйте количество мемов в функции get_meme_name()
##


def get_meme_name():

    ##
    ## Если загрузили новый мем - вместо числа 5 укажите количество ваших мемов
    ##

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
    sendHelp = types.KeyboardButton('/help')

    ##
    ## Чтобы добавить новую кнопку, напишите:
    ##
    ## button = types.KeyboardButton('<текст>')
    ##
    ## где button - имя переменной, <текст> - текст, который отправится при нажатии на кнопку
    ##

    markup.row(sendAnekgot, sendMemes).add(sendHelp)

    ##
    ## после чего к 52 строчке допишите .add(button)
    ##

    ## Здесь можно поменять текст сообщения
    bot.send_message(m.chat.id, 'Привет, это Telegram чат-бот из мастер-класса «Изобретариума», который мы будем программировать с детьми.', reply_markup=markup)

@bot.message_handler(commands=['help'])
def help(m):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Официальный сайт", url="https://izobretarium.ru"))
    markup.add(types.InlineKeyboardButton("Ссылка на исходник", url="https://github.com/ddybka/izobmk-python-chat-bot"))
    markup.add(types.InlineKeyboardButton("Связаться с автором", url="https://ddybka.t.me"))

    ##
    ## Чтобы добавить новую кнопку, напишите:
    ##
    ## markup.add(types.InlineKeyboardButton("<текст_кнопки>", url="<url>"))
    ##
    ## где <текст_кнопки> - текст, который будет отображаться на кнопке
    ##     <url>          - адрес, который будет открывать кнопка
    ##

    ## Здесь можно поменять текст сообщения
    bot.send_message(m.chat.id, "Ну мы тут делаем своего чат-бота, пользуйтесь!", reply_markup=markup)


##
## TEXT
##

@bot.message_handler(content_types=['text'])
def send_text(m):
    text = m.text.lower()
    print(m)
    print(text)

    if text == "рассказать анекдот":
        bot.send_message(m.chat.id, get_anecdote())
    elif text == "отправить мемчик":
        meme = [types.InputMediaPhoto(open(get_meme_name(), 'rb'))]
        bot.send_media_group(m.chat.id, meme)

    ##
    ## Чтобы добавить новый ответ от бота, напишите:
    ##
    ## elif text == "<ваш_текст>":
    ##   bot.send_media_group(m.chat.id, "<ответ_от_бота>")
    ##
    ## где <ваш_текст>     - сообщение пользователя, на которое отреагирует бот
    ##     <ответ_от_бота> - сообщение бота, которое он напишет на сообщение пользователя
    ##


##
## RUN
##

if __name__ == "__main__":
    bot.polling(none_stop=True)

print("Завершение работы бота...")
