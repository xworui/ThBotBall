import telebot
from telebot import types
import random


bot = telebot.TeleBot('5616482633:AAFBlC3mIWaXx8-syrPJFK-PucF4NM9WsQs')


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

@bot.message_handler(commands=['website'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить", url="https://vk.com/nikitagaidukov"))
    bot.send_message(message.chat.id, 'Вау', reply_markup=markup)

@bot.message_handler(commands=['button'])
def button(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    ball = types.KeyboardButton('/ball')
    comp = types.KeyboardButton('/comp')
    markup.add(ball, comp)
    bot.send_message(message.chat.id, 'Кнопки появились', reply_markup=markup)

bot.polling(none_stop=True)