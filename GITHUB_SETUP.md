# Инструкция: Загрузка проекта на GitHub

## Шаг 1: Авторизация на GitHub

Если у вас ещё нет авторизации, выполните:

```bash
gh auth login
```

Или используйте альтернативный способ:

1. Откройте https://github.com/login/device
2. Введите код: `E2D3-2CBA`
3. Авторизуйтесь

## Шаг 2: Создание репозитория

После авторизации выполните команды:

```bash
# Создать репозиторий на GitHub
gh repo create tiktok-bot --public --source=. --remote=origin

# Отправить код на GitHub
git push -u origin master
```

## Альтернатива: Через веб-интерфейс

1. Откройте https://github.com/new
2. Создайте репозиторий с именем `tiktok-bot`
3. Затем выполните:

```bash
git remote add origin https://github.com/SilentPrince222/tiktok-bot.git
git branch -M main
git push -u origin main
```

## Результат

После успешной загрузки ваш проект будет доступен по адресу:
https://github.com/SilentPrince222/tiktok-bot