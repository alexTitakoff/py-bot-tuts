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

# upd = get_updates()
# # print(json.dumps(upd['result'][-1], indent=2, sort_keys=True))
# last_upd = upd['result'][-1]
# message_from_user = last_upd['message']
# # print(json.dumps(message_from_user, indent=2, sort_keys=True))



# @bot.message_handler(content_types=['text'])
# @bot.message_handler(func=lambda message: True, content_types=['text'])
@bot.message_handler(content_types=['text'])
def handle_text(message):
    answer = "Привет чтобы начать играть наберите комманду /game_start"
    if message.text == 'a':
        answer = 'b'
        bot.send_message(message.chat.id, 'b')
        log(message,answer)
    elif message.text == 'b':
        answer = 'c'
        bot.send_message(message.chat.id, 'c')
        log(message, answer)
    else:
        bot.send_message(message.chat.id, 'Хелло')
        log(message, answer)



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



bot.polling(none_stop=True, interval=0)