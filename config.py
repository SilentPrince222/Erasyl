import os
from dotenv import load_dotenv

# Загружаем переменные окружения из файла .env
load_dotenv()

# Токен Telegram бота
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Проверяем, что токен установлен
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не найден в файле .env")