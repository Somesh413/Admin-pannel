# main.py (Telegram Bot Start Button Code)
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "7215344264:AAH_-h_D-DA_fZKPMLH98NQhAFRb_w3OF30"  # Replace this

MINI_APP_URL = "https://cute-twilight-6eefd1.netlify.app"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    keyboard = [[InlineKeyboardButton("🚀 Start Earning", url=MINI_APP_URL)]]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await context.bot.send_photo(
        chat_id=update.effective_chat.id,
        photo="https://freeimage.host/i/FMntULN",  # Replace with your image
        caption=(
            f"👋 Hi {user.first_name}!\n\n"
            "Welcome to *Fast Paisa Mini App* 💸\n\n"
            "✅ Earn by completing tasks\n"
            "✅ Spin & Win daily\n"
            "✅ Refer & Earn ₹5 per friend\n\n"
            "👇 Tap below to Start Earning!"
        ),
        parse_mode="Markdown",
        reply_markup=reply_markup
    )

if __name__ == '__main__':
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot is running...")
    app.run_polling()
