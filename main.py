import requests
import telebot
import config
import time

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


# Типо справочник юзера TODO: разобраться что за тип данных и как в него заносится
user_dict = {}


# Типо собирает объект юзера кажись в итоге .
# // Но тогда вопрос зачем справочник ? или что можеть
# делать спраочник чего не можт объект и наоборот
class User:
    def __init__(self, name):
        self.name = name
        self.age = None
        self.sex = None

user = User('null')



class MainState:
    pass


# Определяем состояние всего бота
main_state = MainState()
main_state.start = False
main_state.name = False


@bot.message_handler(commands=['start_reg'])
def start_reg_handler(message):
    import modules.registration
    modules.registration.init(message,bot,user)




@bot.message_handler(commands=['start'])
def init_commands(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/start_reg', 'отмена')
    user_markup.one_time_keyboard = True  # скрытие после выбора

    bot.send_message(message.from_user.id, 'Привет вот стартовые комманды', reply_markup=user_markup)






# my test chat.id   125875089
#
# def send_info():
#     bot.send_message(125875089, 'Тут вот какая то информация для общей рассылки')


# Отпрвка мессаджа
# time.sleep(10)
# send_info()

#
# while True:
#     time.sleep(2)
#     print(get_updates())

bot.polling(none_stop=True, interval=0)
