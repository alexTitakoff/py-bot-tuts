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


class MainState:
    pass


# Определяем состояние всего бота
main_state = MainState()
main_state.start = False
main_state.name = False


@bot.message_handler(commands=['start_reg'])
def start_reg(message):
    bot.send_message(message.from_user.id, 'Начало регистрации')
    main_state.start = True  # зашли в хук

    msg = bot.reply_to(message, """\
    Hi there, I am Example bot.
    What's your name?
    """)
    bot.register_next_step_handler(msg, process_name_step)


def process_name_step(message):
    try:
        chat_id = message.chat.id
        name = message.text
        print(name)
        # user = User(name)
        # user_dict[chat_id] = user
        msg = bot.reply_to(message, 'How old are you?')
        bot.register_next_step_handler(msg, next_step)
    except Exception as e:
        bot.reply_to(message, 'oooops')


def next_step(message):
    print('Next step work!')


@bot.message_handler(commands=['start'])
def init_commands(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('/start_reg', 'отмена')
    user_markup.one_time_keyboard = True  # скрытие после выбора

    bot.send_message(message.from_user.id, 'Привет вот стартовые комманды', reply_markup=user_markup)


bot.polling(none_stop=True, interval=0)
