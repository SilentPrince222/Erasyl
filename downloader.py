"""
Модуль для скачивания видео из TikTok
"""
import asyncio
import logging
import os
import uuid
import yt_dlp
from config import DOWNLOAD_FOLDER

logger = logging.getLogger(__name__)


class TikTokDownloader:
    """Класс для скачивания видео из TikTok"""
    
    def __init__(self):
        self.download_folder = DOWNLOAD_FOLDER
        os.makedirs(self.download_folder, exist_ok=True)
    
    async def download_video(self, url: str) -> str | None:
        """
        Скачивание видео из TikTok
        
        Args:
            url: URL видео из TikTok
            
        Returns:
            Путь к скачанному видео или None при ошибке
        """
        try:
            # Генерируем уникальное имя файла
            filename = f"{uuid.uuid4().hex}.mp4"
            filepath = os.path.join(self.download_folder, filename)
            
            # Настройки yt-dlp
            ydl_opts = {
                'outtmpl': filepath,
                'format': 'best[ext=mp4]/best',
                'quiet': True,
                'no_warnings': True,
                'extractaudio': False,
                'noplaylist': True,
                'rm_cachedir': True,
                # Удаляем водяной знак
                'postprocessors': [],
            }
            
            # Запускаем скачивание в отдельном потоке
            loop = asyncio.get_event_loop()
            
            def download():
                with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                    ydl.download([url])
            
            await loop.run_in_executor(None, download)
            
            # Проверяем, что файл скачался
            if os.path.exists(filepath):
                logger.info(f"Видео успешно скачано: {filepath}")
                return filepath
            else:
                logger.error(f"Файл не найден: {filepath}")
                return None
                
        except Exception as e:
            logger.error(f"Ошибка при скачивании видео: {e}")
            return None
    
    def cleanup(self, filepath: str):
        """Удаление временного файла"""
        try:
            if os.path.exists(filepath):
                os.remove(filepath)
                logger.info(f"Файл удален: {filepath}")
        except Exception as e:
            logger.error(f"Ошибка при удалении файла: {e}")