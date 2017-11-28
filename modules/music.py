import telebot
import config

bot = telebot.TeleBot(config.token)


def init(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True, False)
    user_markup.row('hip-hop', 'trip-hop', 'jazz', 'chill')
    user_markup.one_time_keyboard = True  # скрытие после выбора

    bot.send_message(message.from_user.id, 'Какие виды музыки тебе нравятся?', reply_markup=user_markup)

