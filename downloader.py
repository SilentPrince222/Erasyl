import yt_dlp
import os
import uuid
import re

# Папка для скачивания видео
DOWNLOADS_DIR = "downloads"

# Убедимся, что папка существует
os.makedirs(DOWNLOADS_DIR, exist_ok=True)


def is_tiktok_url(url: str) -> bool:
    """Проверяет, является ли URL ссылкой на TikTok"""
    tiktok_patterns = [
        r'https?://(?:www\.)?tiktok\.com/@[\w.-]+/video/\d+',
        r'https?://(?:vm|vt)\.tiktok\.com/[\w]+',
        r'https?://(?:www\.)?tiktok\.com/t/[\w]+',
    ]
    return any(re.match(pattern, url) for pattern in tiktok_patterns)


def download_tiktok_video(url: str) -> str | None:
    """
    Скачивает видео из TikTok по URL
    
    Args:
        url: Ссылка на видео TikTok
        
    Returns:
        Путь к скачанному файлу или None при ошибке
    """
    # Генерируем уникальное имя файла
    filename = f"{uuid.uuid4()}.mp4"
    filepath = os.path.join(DOWNLOADS_DIR, filename)
    
    # Настройки для yt-dlp
    ydl_opts = {
        'outtmpl': filepath,
        'format': 'best[ext=mp4]/best',
        'quiet': True,
        'no_warnings': True,
        'extractaudio': False,
        'noplaylist': True,
        # Удаляем водяной знак TikTok (если возможно)
        'postprocessors': [],
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        # Проверяем, что файл существует
        if os.path.exists(filepath):
            return filepath
        return None
        
    except Exception as e:
        print(f"Ошибка при скачивании: {e}")
        # Удаляем частично скачанный файл, если есть
        if os.path.exists(filepath):
            os.remove(filepath)
        return None


def cleanup_file(filepath: str) -> None:
    """Удаляет файл после отправки"""
    try:
        if os.path.exists(filepath):
            os.remove(filepath)
    except Exception as e:
        print(f"Ошибка при удалении файла: {e}")