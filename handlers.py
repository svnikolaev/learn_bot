from glob import glob
from random import choice

from utils import get_smile, play_random_numbers, main_keyboard

def greet_user(update, context):
    smile = get_smile(context.user_data, change_smile=True)
    context.user_data['emoji'] = smile
    # my_keyboard = ReplyKeyboardMarkup([['/cat']])
    update.message.reply_text(
        f"Здравствуй, пользователь {smile}!", 
        reply_markup=main_keyboard()
    )

def talk_to_me(update, context):
    smile = get_smile(context.user_data)
    text = update.message.text
    print(text)
    update.message.reply_text(
        f"{text}, {smile}!"
    )

def guess_number(update, context):
    if context.args:
        try:
            user_number = int(context.args[0])
            message = play_random_numbers(user_number)
        except(TypeError, ValueError):
            message = "Нужно ввести целое число"
    else:
        message = "Введи число"
    update.message.reply_text(
        message
    )

def send_cat_picture(update, context):
    cat_photos_list = glob('images/cat*')
    cat_pic_filename = choice(cat_photos_list)
    chat_id = update.effective_chat.id 
    context.bot.send_photo(chat_id=chat_id, photo=open(cat_pic_filename, 'rb'))

def user_coordinates(update, context):
    smile = get_smile(context.user_data)
    coords = update.message.location
    update.message.reply_text(
        f"Ваши координаты {coords} {smile}!",
        reply_markup=main_keyboard()
    )