# Проект LearnBot

LearnBot - это бот для Telegram, на котором я учусь, он умеет присылать котиков

## Установка

1. Клонировать репозиторий с github
2. Создать и активировать виртуальное окружение 
    * для создания в директории проекта выполните `python3 -m venv env` 
    * для активации в директории проекта выполните `source ./env/bin/activate`
3. Установить зависимости `pip install -r requirements.txt`
4. Создать файл `local_settings.py`, который имеет структуру:
```
TELEGRAM_BOT_TOKEN = "bot_secret_token"
USER_EMOJI = [':smiley_cat:', ':smiling_imp:', ':panda_face:', ':dog:']
```
5. Запустить бота командой `python mybot.py`