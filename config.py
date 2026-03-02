"""
Конфигурация бота
"""
import os
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()

# Токен Telegram бота
BOT_TOKEN = os.getenv("BOT_TOKEN")

# Папка для скачивания видео
DOWNLOAD_FOLDER = os.path.join(os.path.dirname(__file__), "downloads")

# Создаем папку для скачивания, если не существует
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)