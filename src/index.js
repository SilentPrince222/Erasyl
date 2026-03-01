import { Bot, webhookCallback } from "grammy";

// Инициализация бота
const bot = new Bot(process.env.BOT_TOKEN);

// Проверка TikTok URL
function isTiktokUrl(url) {
    const patterns = [
        /^https?:\/\/(?:www\.)?tiktok\.com\/@[\w.-]+\/video\/\d+/,
        /^https?:\/\/(?:vm|vt)\.tiktok\.com\/[\w]+/,
        /^https?:\/\/(?:www\.)?tiktok\.com\/t\/[\w]+/,
    ];
    return patterns.some(pattern => pattern.test(url));
}

// Команда /start
bot.command("start", async (ctx) => {
    const welcomeText = `👋 Привет! Я бот для скачивания видео из TikTok.

📌 Просто отправь мне ссылку на видео из TikTok, и я скачаю его для тебя.

✅ Поддерживаемые форматы ссылок:
• https://www.tiktok.com/@user/video/...
• https://vm.tiktok.com/...
• https://vt.tiktok.com/...`;

    await ctx.reply(welcomeText);
});

// Команда /help
bot.command("help", async (ctx) => {
    const helpText = `📖 Как пользоваться ботом:

1. Скопируй ссылку на видео из TikTok
2. Отправь ссылку мне в чат
3. Получи видео!

Команды:
/start - Начать работу с ботом
/help - Показать справку`;

    await ctx.reply(helpText);
});

// Обработка текстовых сообщений
bot.on("message:text", async (ctx) => {
    const url = ctx.message.text.trim();

    if (!isTiktokUrl(url)) {
        await ctx.reply(
            "❌ Это не похоже на ссылку из TikTok.\n" +
            "Пожалуйста, отправь корректную ссылку на видео."
        );
        return;
    }

    const statusMessage = await ctx.reply("⏳ Скачиваю видео...");

    try {
        // Скачиваем видео через TikTok API
        const videoUrl = await getTiktokVideoUrl(url);

        if (videoUrl) {
            await ctx.replyWithVideo(videoUrl, {
                caption: "✅ Видео успешно скачано!"
            });
            await ctx.api.deleteMessage(ctx.chat.id, statusMessage.message_id);
        } else {
            await ctx.api.editMessageText(
                ctx.chat.id,
                statusMessage.message_id,
                "❌ Не удалось скачать видео. Возможно, оно недоступно или ссылка некорректна."
            );
        }
    } catch (error) {
        console.error("Ошибка:", error);
        await ctx.api.editMessageText(
            ctx.chat.id,
            statusMessage.message_id,
            "❌ Произошла ошибка при скачивании видео. Попробуй ещё раз."
        );
    }
});

// Функция для получения URL видео из TikTok
async function getTiktokVideoUrl(tiktokUrl) {
    try {
        // Используем публичный API для получения видео
        const apiUrl = `https://www.tikwm.com/api/?url=${encodeURIComponent(tiktokUrl)}`;

        const response = await fetch(apiUrl, {
            headers: {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
            }
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();

        if (data.code === 0 && data.data) {
            // Возвращаем URL видео без водяного знака
            return data.data.play || data.data.wmplay || null;
        }

        return null;
    } catch (error) {
        console.error("Ошибка при получении видео:", error);
        return null;
    }
}

// Webhook обработчик для Cloudflare Workers
const handleWebhook = webhookCallback(bot, "fetch");

// Основной обработчик
export default {
    async fetch(request, env, ctx) {
        // Устанавливаем токен из переменных окружения
        bot.token = env.BOT_TOKEN;

        // Обработка webhook
        return handleWebhook(request);
    }
};