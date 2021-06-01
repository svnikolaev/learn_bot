from emoji import emojize
from random import randint, choice
from telegram import ReplyKeyboardMarkup, KeyboardButton

import local_settings

def get_smile(user_data, change_smile=False):
    if 'emoji' not in user_data or change_smile:
        smile = choice(local_settings.USER_EMOJI)
        return emojize(smile, use_aliases=True)
    return user_data['emoji']

def play_random_numbers(user_number):
    bot_number = randint(user_number - 10, user_number + 10)
    return f"{user_number} > {bot_number}: Вы выйграли" if user_number > bot_number else f"{user_number} < {bot_number}: Вы проиграли" if user_number < bot_number else "Ничья"

def main_keyboard():
    return ReplyKeyboardMarkup([['Прислать котика', KeyboardButton('Мои координаты', request_location=True)]], resize_keyboard=True)