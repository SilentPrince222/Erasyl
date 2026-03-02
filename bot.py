"""
Telegram бот для скачивания видео из TikTok
"""
import asyncio
import logging
import os
import re
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import FSInputFile
from dotenv import load_dotenv

from downloader import TikTokDownloader

# Загрузка переменных окружения
load_dotenv()

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Токен бота
BOT_TOKEN = os.getenv("BOT_TOKEN")
if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не найден в переменных окружения!")

# Инициализация бота
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Инициализация загрузчика
downloader = TikTokDownloader()


def is_tiktok_url(url: str) -> bool:
    """Проверка, является ли URL ссылкой на TikTok"""
    patterns = [
        r'^https?://(?:www\.)?tiktok\.com/@[\w.-]+/video/\d+',
        r'^https?://(?:vm|vt)\.tiktok\.com/[\w]+',
        r'^https?://(?:www\.)?tiktok\.com/t/[\w]+',
    ]
    return any(re.match(pattern, url) for pattern in patterns)


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    """Обработка команды /start"""
    welcome_text = """👋 Привет! Я бот для скачивания видео из TikTok.

📌 Просто отправь мне ссылку на видео из TikTok, и я скачаю его для тебя.

✅ Поддерживаемые форматы ссылок:
• https://www.tiktok.com/@user/video/...
• https://vm.tiktok.com/...
• https://vt.tiktok.com/..."""
    
    await message.answer(welcome_text)


@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    """Обработка команды /help"""
    help_text = """📖 Как пользоваться ботом:

1. Скопируй ссылку на видео из TikTok
2. Отправь ссылку мне в чат
3. Получи видео!

Команды:
/start - Начать работу с ботом
/help - Показать справку"""
    
    await message.answer(help_text)


@dp.message(F.text)
async def handle_message(message: types.Message):
    """Обработка текстовых сообщений"""
    url = message.text.strip()
    
    if not is_tiktok_url(url):
        await message.answer(
            "❌ Это не похоже на ссылку из TikTok.\n"
            "Пожалуйста, отправь корректную ссылку на видео."
        )
        return
    
    status_message = await message.answer("⏳ Скачиваю видео...")
    
    try:
        # Скачиваем видео
        video_path = await downloader.download_video(url)
        
        if video_path and os.path.exists(video_path):
            # Отправляем видео
            video = FSInputFile(video_path)
            await message.answer_video(video, caption="✅ Видео успешно скачано!")
            await status_message.delete()
            
            # Удаляем временный файл
            try:
                os.remove(video_path)
            except:
                pass
        else:
            await status_message.edit_text(
                "❌ Не удалось скачать видео. Возможно, оно недоступно или ссылка некорректна."
            )
    except Exception as e:
        logger.error(f"Ошибка при обработке видео: {e}")
        await status_message.edit_text(
            "❌ Произошла ошибка при скачивании видео. Попробуй ещё раз."
        )


async def main():
    """Запуск бота"""
    logger.info("Запуск бота...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())