import logging
from emoji import emojize
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from random import randint, choice
from glob import glob

import local_settings

logging.basicConfig(filename='bot.log', level=logging.INFO)

def get_smile(user_data, change_smile=False):
    if 'emoji' not in user_data or change_smile:
        smile = choice(local_settings.USER_EMOJI)
        return emojize(smile, use_aliases=True)
    return user_data['emoji']

def greet_user(update, context):
    smile = get_smile(context.user_data, change_smile=True)
    context.user_data['emoji'] = smile
    logging.info("Вызван /start")
    update.message.reply_text(f"Здравствуй, пользователь {smile}!")

def play_random_numbers(user_number):
    bot_number = randint(user_number - 10, user_number + 10)
    return f"{user_number} > {bot_number}: Вы выйграли" if user_number > bot_number else f"{user_number} < {bot_number}: Вы проиграли" if user_number < bot_number else "Ничья"

def guess_number(update, context):
    # print(context.args)
    if context.args:
        try:
            user_number = int(context.args[0])
            message = play_random_numbers(user_number)
        except(TypeError, ValueError):
            message = "Нужно ввести целое число"
    else:
        message = "Введи число"
    update.message.reply_text(message)

def talk_to_me(update, context):
    smile = get_smile(context.user_data)
    text = update.message.text
    print(text)
    update.message.reply_text(f"{text}, {smile}!")

def send_cat_picture(update, context):
    cat_photos_list = glob('images/cat*')
    cat_pic_filename = choice(cat_photos_list)
    chat_id = update.effective_chat.id 
    context.bot.send_photo(chat_id=chat_id, photo=open(cat_pic_filename, 'rb'))

def main():
    mybot = Updater(token=local_settings.TELEGRAM_BOT_TOKEN, use_context=True)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("guess", guess_number))
    dp.add_handler(CommandHandler("cat", send_cat_picture))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    logging.info("Бот стартовал")
    mybot.start_polling()
    mybot.idle()

if __name__ == "__main__":
    main()