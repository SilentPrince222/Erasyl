# Деплой Telegram бота на PythonAnywhere

## Шаг 1: Регистрация на PythonAnywhere

1. Перейдите на https://www.pythonanywhere.com/
2. Нажмите "Create a free account"
3. Заполните форму регистрации
4. Подтвердите email

## Шаг 2: Создание веб-приложения

1. После входа перейдите на вкладку **Web**
2. Нажмите **Add a new web app**
3. Выберите ваш домен (например: `ваше_имя.pythonanywhere.com`)
4. Выберите **Manual configuration**
5. Выберите **Python 3.10** или новее

## Шаг 3: Загрузка файлов

### Вариант A: Через Git (рекомендуется)

1. Откройте вкладку **Consoles** → **Bash**
2. Клонируйте репозиторий:
```bash
git clone https://github.com/ВАШ_ЮЗЕРНЕЙМ/tiktok-bot.git
cd tiktok-bot
```

### Вариант B: Через веб-интерфейс

1. Откройте вкладку **Files**
2. Создайте папку `tiktok-bot`
3. Загрузите файлы:
   - `bot.py`
   - `config.py`
   - `downloader.py`
   - `requirements.txt`

## Шаг 4: Настройка виртуального окружения

1. Откройте вкладку **Consoles** → **Bash**
2. Создайте виртуальное окружение:
```bash
mkvirtualenv tiktok-env --python=/usr/bin/python3.10
```

3. Установите зависимости:
```bash
cd tiktok-bot
pip install -r requirements.txt
```

## Шаг 5: Настройка переменных окружения

1. Откройте вкладку **Web**
2. Найдите раздел **Environment variables**
3. Добавьте переменную:
   - Имя: `BOT_TOKEN`
   - Значение: `8778926357:AAHm2GrLp9DvsgjlnIFrEMdJKtIKTOF7ibM`

## Шаг 6: Настройка WSGI файла

1. Откройте вкладку **Web**
2. Найдите раздел **Code** → **WSGI configuration file**
3. Нажмите на ссылку на файл
4. Замените содержимое на:

```python
import sys
import os

# Добавляем путь к проекту
path = '/home/ВАШЕ_ИМЯ/tiktok-bot'
if path not in sys.path:
    sys.path.append(path)

# Устанавливаем переменные окружения
os.environ['BOT_TOKEN'] = '8778926357:AAHm2GrLp9DvsgjlnIFrEMdJKtIKTOF7ibM'

# Импортируем и запускаем бота
from bot import main
import asyncio

# Для webhook режима (если нужен)
# application = bot.app
```

## Шаг 7: Запуск бота (Always-on task)

На бесплатном тарифе бот будет работать ограниченное время. Для постоянной работы:

### На бесплатном тарифе:
Используйте **Scheduled tasks** для периодического запуска:
1. Откройте вкладку **Tasks**
2. Создайте задачу:
   - Command: `cd /home/ВАШЕ_ИМЯ/tiktok-bot && /home/ВАШЕ_ИМЯ/.virtualenvs/tiktok-env/bin/python bot.py`
   - Hourly или каждые несколько часов

### На платном тарифе ($5/месяц):
1. Откройте вкладку **Consoles** → **Bash**
2. Запустите бота:
```bash
workon tiktok-env
cd tiktok-bot
python bot.py
```
3. Бот будет работать постоянно (Always-on)

## Шаг 8: Проверка

1. Откройте Telegram
2. Найдите бота: @hfdjshfn_BOT
3. Отправьте `/start`
4. Отправьте ссылку на TikTok видео

## Альтернатива: Webhook режим

Для работы через webhook (лучше для бесплатного тарифа):

1. Измените `bot.py` для использования webhook
2. Настройте URL: `https://ваше_имя.pythonanywhere.com/webhook`
3. Бот будет отвечать только на запросы Telegram

## Полезные команды

```bash
# Активировать виртуальное окружение
workon tiktok-env

# Деактивировать
deactivate

# Посмотреть логи
tail -f /var/log/ваше_имя.log

# Перезапустить веб-приложение
# Через вкладку Web → кнопка Reload
```

## Ограничения бесплатного тарифа

- 512 MB дискового пространства
- Ограниченное CPU время
- Нет Always-on tasks
- Бот может "засыпать"

Для постоянной работы бота рекомендуется платный тариф ($5/месяц).