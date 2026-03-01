# TikTok Video Downloader Bot

Telegram бот для скачивания видео из TikTok.

## Структура проекта

```
├── bot.py                  # Основной код бота (Python)
├── config.py               # Конфигурация и переменные окружения
├── downloader.py           # Модуль для скачивания видео
├── run_bot.py              # Скрипт запуска для PythonAnywhere
├── requirements.txt        # Зависимости Python
├── .env                    # Переменные окружения (не в git)
├── .env.example            # Пример файла .env
├── pythonanywhere_setup.md # Инструкции для PythonAnywhere
└── downloads/              # Папка для временных видео
```

## Быстрый старт (локально)

### 1. Установка зависимостей

```bash
pip install -r requirements.txt
```

### 2. Настройка переменных окружения

Создайте файл `.env`:
```
BOT_TOKEN=ваш_токен_бота
```

### 3. Запуск

```bash
python bot.py
```

## Деплой на PythonAnywhere (бесплатно)

### Шаг 1: Регистрация

1. Перейдите на https://www.pythonanywhere.com/
2. Создайте бесплатный аккаунт

### Шаг 2: Загрузка файлов

**Через Git:**
```bash
git clone https://github.com/ВАШ_ЮЗЕРНЕЙМ/tiktok-bot.git
```

**Или через веб-интерфейс:**
Загрузите файлы: `bot.py`, `config.py`, `downloader.py`, `requirements.txt`

### Шаг 3: Настройка виртуального окружения

```bash
mkvirtualenv tiktok-env --python=/usr/bin/python3.10
pip install -r requirements.txt
```

### Шаг 4: Настройка переменных окружения

В вкладке **Web** → **Environment variables** добавьте:
- `BOT_TOKEN` = `ваш_токен`

### Шаг 5: Запуск

**Вариант A: Через консоль (платный тариф)**
```bash
workon tiktok-env
python run_bot.py
```

**Вариант B: Scheduled Tasks (бесплатный тариф)**
Создайте задачу в вкладке **Tasks** для периодического запуска.

📖 Подробные инструкции в файле `pythonanywhere_setup.md`

## Команды бота

- `/start` - Приветствие и инструкции
- `/help` - Справка по использованию

## Использование

Просто отправьте ссылку на TikTok видео боту, и он пришлёт скачанное видео.

## Безопасность

- Токен бота хранится в переменных окружения
- `.dev.vars` и `.env` добавлены в `.gitignore`