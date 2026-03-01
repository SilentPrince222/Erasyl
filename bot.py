import asyncio
import logging
import sys
import io

# Исправление кодировки для Windows
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command
from aiogram.types import FSInputFile

from config import BOT_TOKEN
from downloader import is_tiktok_url, download_tiktok_video, cleanup_file

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    """Обработчик команды /start"""
    welcome_text = (
        "👋 Привет! Я бот для скачивания видео из TikTok.\n\n"
        "📌 Просто отправь мне ссылку на видео из TikTok, "
        "и я скачаю его для тебя без водяного знака.\n\n"
        "✅ Поддерживаемые форматы ссылок:\n"
        "• https://www.tiktok.com/@user/video/...\n"
        "• https://vm.tiktok.com/...\n"
        "• https://vt.tiktok.com/..."
    )
    await message.answer(welcome_text)


@dp.message(Command("help"))
async def cmd_help(message: types.Message):
    """Обработчик команды /help"""
    help_text = (
        "📖 Как пользоваться ботом:\n\n"
        "1. Скопируй ссылку на видео из TikTok\n"
        "2. Отправь ссылку мне в чат\n"
        "3. Получи видео без водяного знака!\n\n"
        "Команды:\n"
        "/start - Начать работу с ботом\n"
        "/help - Показать справку"
    )
    await message.answer(help_text)


@dp.message(F.text)
async def handle_message(message: types.Message):
    """Обработчик текстовых сообщений (ссылок)"""
    url = message.text.strip()
    
    # Проверяем, является ли сообщение ссылкой на TikTok
    if not is_tiktok_url(url):
        await message.answer(
            "❌ Это не похоже на ссылку из TikTok.\n"
            "Пожалуйста, отправь корректную ссылку на видео."
        )
        return
    
    # Отправляем сообщение о начале загрузки
    status_message = await message.answer("⏳ Скачиваю видео...")
    
    # Скачиваем видео (выполняем в отдельном потоке, чтобы не блокировать event loop)
    filepath = await asyncio.to_thread(download_tiktok_video, url)
    
    if filepath:
        try:
            # Отправляем видео
            video = FSInputFile(filepath)
            await message.answer_video(
                video,
                caption="✅ Видео успешно скачано!"
            )
            await status_message.delete()
        except Exception as e:
            logging.error(f"Ошибка при отправке видео: {e}")
            await status_message.edit_text(
                "❌ Произошла ошибка при отправке видео. Попробуй ещё раз."
            )
        finally:
            # Удаляем временный файл
            cleanup_file(filepath)
    else:
        await status_message.edit_text(
            "❌ Не удалось скачать видео. Возможно, оно недоступно "
            "или ссылка некорректна. Попробуй другую ссылку."
        )


async def main():
    """Запуск бота"""
    print("🤖 Бот запущен!")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())