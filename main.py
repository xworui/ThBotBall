import telebot
from telebot import types
import random


bot = telebot.TeleBot('5616482633:AAFBlC3mIWaXx8-syrPJFK-PucF4NM9WsQs')


@bot.message_handler(command=['qp'])
def qp(message):
    markup = types.ReplyKeyboardMarkup()
    website = types.KeyboardButton('BOOB')
    qwp = types.KeyboardButton('qwp')
    markup.add(website, qwp)
    bot.send_message(message.chat.id, 'Бам', reply_markup=markup)


@bot.message_handler(commands=['ball'])
def ball(message):
    mess = ['да', 'нет',  'наверное', 'может быть', 'спроси позже', 'херня', 'отличная идея', 'есть шанс', 'прекрасная возможность', 'забудь',' не думай об этом']
    bot.send_message(message.chat.id, random.choice(mess))

@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Че старт пишешь {message.from_user.first_name}, /help писать надо'
    bot.send_message(message.chat.id, mess)

@bot.message_handler(commands=['comp'])
def comp(message):
    mess = ['ты невероятая', 'ты самая лучшая', 'ты самая красивая', 'ты самая милая', 'я люблю тебя', 'ты моя принцесса', 'я тебя обожаю', 'ты даришь мне радость', 'у тебя самые красивый глаза', 'у тебя классная попа', 'у тебя прекрасные волосы', 'ты вкусно пахнешь']
    bot.send_message(message.chat.id, random.choice(mess))

@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, 'Шарик - /ball\nКомплимент - /comp\nРофл команда - /start')




#@bot.message_handler()
#def get_user_text(message):
#    if message.text == "Привет":
#        bot.send_message(message.chat.id, "BOOOO")
#    else:
#        bot.send_message(message.chat.id, "Пиши /help, а не ерунду всякую")



bot.polling(none_stop=True)