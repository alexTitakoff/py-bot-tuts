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
@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_text(message):
    print('-- handler')
    if message.text == 'a':
        bot.send_message(message.chat.id, 'b')
    elif message.text == 'b':
        bot.send_message(message.chat.id, 'c')
    else:
        bot.send_message(message.chat.id, 'Хелло')




bot.polling(none_stop=True, interval=0)