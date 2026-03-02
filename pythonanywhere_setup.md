# Деплой Telegram бота на PythonAnywhere

## Ваш аккаунт: https://www.pythonanywhere.com/user/SilentPrince4/

---

## Шаг 1: Загрузка файлов

### Вариант A: Через Git (рекомендуется)

1. Откройте **Bash консоль**: https://www.pythonanywhere.com/user/SilentPrince4/consoles/
2. Клонируйте репозиторий:
```bash
git clone https://github.com/SilentPrince222/tiktok-bot.git
cd tiktok-bot
```

### Вариант B: Через веб-интерфейс

1. Откройте **Files**: https://www.pythonanywhere.com/user/SilentPrince4/files/
2. Создайте папку `tiktok-bot`
3. Загрузите файлы:
   - `bot.py`
   - `config.py`
   - `downloader.py`
   - `requirements.txt`
   - `run_bot.py`

---

## Шаг 2: Настройка виртуального окружения

1. Откройте **Bash консоль**: https://www.pythonanywhere.com/user/SilentPrince4/consoles/
2. Выполните команды:

```bash
# Создать виртуальное окружение
mkvirtualenv tiktok-env --python=/usr/bin/python3.10

# Перейти в папку проекта
cd tiktok-bot

# Установить зависимости
pip install -r requirements.txt
```

---

## Шаг 3: Настройка переменных окружения

1. Откройте **Web**: https://www.pythonanywhere.com/user/SilentPrince4/web_app_setup/
2. Или откройте **Bash консоль** и создайте файл `.env`:

```bash
cd ~/tiktok-bot
echo "BOT_TOKEN=8778926357:AAHm2GrLp9DvsgjlnIFrEMdJKtIKTOF7ibM" > .env
```

---

## Шаг 4: Запуск бота (Always-on task)

### Для платного тарифа ($5/месяц) - Always-on task:

1. Откройте **Tasks**: https://www.pythonanywhere.com/user/SilentPrince4/tasks/
2. Создайте **Always-on task**:
   - Command: `cd /home/SilentPrince4/tiktok-bot && /home/SilentPrince4/.virtualenvs/tiktok-env/bin/python bot.py`
   - Description: `TikTok Telegram Bot`

### Для бесплатного тарифа - Scheduled task:

1. Откройте **Tasks**: https://www.pythonanywhere.com/user/SilentPrince4/tasks/
2. Создайте **Scheduled task**:
   - Command: `cd /home/SilentPrince4/tiktok-bot && /home/SilentPrince4/.virtualenvs/tiktok-env/bin/python bot.py`
   - Hour: выберите час (например, 0)
   - Бот будет запускаться раз в час

---

## Шаг 5: Проверка

1. Откройте Telegram
2. Найдите бота: @hfdjshfn_BOT
3. Отправьте `/start`
4. Отправьте ссылку на TikTok видео

---

## Быстрые ссылки:

- **Dashboard**: https://www.pythonanywhere.com/user/SilentPrince4/
- **Consoles**: https://www.pythonanywhere.com/user/SilentPrince4/consoles/
- **Files**: https://www.pythonanywhere.com/user/SilentPrince4/files/
- **Tasks**: https://www.pythonanywhere.com/user/SilentPrince4/tasks/
- **Web**: https://www.pythonanywhere.com/user/SilentPrince4/web_app_setup/

---

## Полезные команды в консоли:

```bash
# Активировать виртуальное окружение
workon tiktok-env

# Перейти в папку проекта
cd ~/tiktok-bot

# Запустить бота вручную
python bot.py

# Посмотреть логи
tail -f ~/tiktok-bot/bot.log

# Деактивировать окружение
deactivate
```

---

## Ограничения бесплатного тарифа:

- 512 MB дискового пространства
- Ограниченное CPU время
- Нет Always-on tasks
- Scheduled tasks работают раз в час

**Для постоянной работы бота рекомендуется платный тариф ($5/месяц)** - это даст Always-on task, который будет работать 24/7.