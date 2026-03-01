#!/usr/bin/env python3
"""
Скрипт для запуска бота на PythonAnywhere
Запускается через Scheduled Tasks или в консоли
"""
import sys
import os

# Добавляем текущую директорию в путь
current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

# Импортируем и запускаем бота
from bot import main
import asyncio

if __name__ == "__main__":
    print("Запуск TikTok бота...")
    asyncio.run(main())