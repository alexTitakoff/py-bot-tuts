import telebot
import config
import requests
import json

bot = telebot.TeleBot(config.token)
URL = 'https://api.telegram.org/bot' + config.token + '/'


def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    return r.json()


def log(message, answer):
    print('\n ------')
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}. (id={2}) \n Текст - {3}".format(message.from_user.first_name,
                                                                 message.from_user.last_name,
                                                                 str(message.from_user.id),
                                                                 message.text))
    print(answer)


@bot.message_handler(commands=['help'])
def handle_text(message):
    bot.send_message(message.chat.id, 'Это комманда помощи')


@bot.message_handler(commands=['game'])
def handle_text(message):
    bot.send_message(message.chat.id, 'игра городки началась')
    bot.send_message(message.chat.id, 'Оренбург')

    @bot.message_handler(content_types=['text'])
    def handle_text(message):
        print(message.text)


@bot.message_handler(commands=['keyboard'])
def handle_keyboard(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/start', '/hide')
    user_markup.row('фото', 'аудио', 'документы')
    user_markup.row('стикер', 'видео', 'локация')
    user_markup.one_time_keyboard = True  # скрытие после выбора
    bot.send_message(message.from_user.id, 'Добро пожаловать', reply_markup=user_markup)

@bot.message_handler(commands=['hide'])
def hide_keyboard(message):
    # hide_markup = telebot.types.ReplyKeyboardRemove(selective=False)
    # bot.send_message(message.from_user.id,'..', reply_markup=hide_markup)
    print('hide command')

bot.polling(none_stop=True, interval=0)
