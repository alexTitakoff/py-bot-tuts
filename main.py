import requests
import telebot
import config

bot = telebot.TeleBot(config.token)
URL = 'https://api.telegram.org/bot' + config.token + '/'


def get_updates():
    url = URL + 'getupdates'
    r = requests.get(url)
    return r.json()


def get_last_updates():
    url = URL + 'getupdates'
    r = requests.get(url)

    if len(r.json()['result']) != 0:
        return r.json()['result'][-1]
    else:
        return None


# @bot.message_handler(content_types=['text'])
# def handle_text(message):
#     l_upd = get_last_updates()
#     print(l_upd['message'])
#     print(l_upd['message']['text'])


# def log(message, answer):
#     print('\n ------')
#     from datetime import datetime
#     print(datetime.now())
#     print("Сообщение от {0} {1}. (id={2}) \n Текст - {3}".format(message.from_user.first_name,
#                                                                  message.from_user.last_name,
#                                                                  str(message.from_user.id),
#                                                                  message.text))
#     print(answer)
#
#
# @bot.message_handler(commands=['help'])
# def handle_text(message):
#     bot.send_message(message.chat.id, 'Это комманда помощи')
#
#
# @bot.message_handler(commands=['game'])
# def handle_text(message):
#     bot.send_message(message.chat.id, 'игра городки началась')
#     bot.send_message(message.chat.id, 'Оренбург')
#
#     @bot.message_handler(content_types=['text'])
#     def handle_text(message):
#         print(message.text)
#
#
# @bot.message_handler(commands=['keyboard'])
# def handle_keyboard(message):
#     user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
#     user_markup.row('/start', '/hide')
#     user_markup.row('фото', 'аудио', 'документы')
#     user_markup.row('стикер', 'видео', 'локация')
#     user_markup.one_time_keyboard = True  # скрытие после выбора
#     bot.send_message(message.from_user.id, 'Добро пожаловать', reply_markup=user_markup)
#
#
# @bot.message_handler(commands=['hide'])
# def hide_keyboard(message):
#     # hide_markup = telebot.types.ReplyKeyboardRemove(selective=False)
#     # bot.send_message(message.from_user.id,'..', reply_markup=hide_markup)
#     print('hide command')


class MainState:
    pass


# Определяем состояние всего бота
main_state = MainState()
main_state.start = False



@bot.message_handler(commands=['start'])
def hide_keyboard(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('о музыке', 'о котиках')
    user_markup.one_time_keyboard = True  # скрытие после выбора

    bot.send_message(message.from_user.id, 'Привет о чем поговорим?', reply_markup=user_markup)

    main_state.start = True     # зашли в хук


def start_func(message):
    if message.text == 'о музыке':
        bot.send_message(message.chat.id, 'хоршо давай погорим о музыке')

        # импортируем модуль отвечающий за блок музыки
        import modules.music
        modules.music.init(message)

    if message.text == 'о котиках':
        bot.send_message(message.chat.id, 'хоршо давай погорим о котиках')

    main_state.start = False   # выходим из хука


@bot.message_handler(content_types=['text'])
def handle(message):
    print(main_state.start)
    if main_state.start:
        start_func(message)




bot.polling(none_stop=True, interval=0)
