bot_module = ''
user_module = ''


def init(message,bot,user):
    global bot_module
    bot_module = bot

    global user_module
    user_module = user

    print(user_module)

    bot_module.send_message(message.from_user.id, 'Начало регистрации')

    msg = bot_module.reply_to(message, "Привет давай знакоомиться. Как тебя зовут?")
    bot_module.register_next_step_handler(msg, process_name_step)


def process_name_step(message):
    try:
        chat_id = message.chat.id
        name = message.text
        print(name)

        # user_dict[chat_id] = user
        msg = bot_module.reply_to(message, 'How old are you?')
        bot_module.register_next_step_handler(msg, next_step)
    except Exception as e:
        bot_module.reply_to(message, 'oooops')


def next_step(message):
    print('Next step work!')
