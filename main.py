import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler

# Logging setup
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

BOT_TOKEN = "7215344264:AAH_-h_D-DA_fZKPMLH98NQhAFRb_w3OF30"  # From BotFather
MINI_APP_URL = "https://cute-twilight-6eefd1.netlify.app"
WELCOME_IMAGE = "https://freeimage.host/i/FMntULN"

def start(update, context):
    try:
        # Create button that opens your mini app
        keyboard = [
            [InlineKeyboardButton("💰 Start Earning", url=MINI_APP_URL)],
            [InlineKeyboardButton("📢 Join Channel", url="https://t.me/yourchannel")]
        ]
        
        # Send message with image and buttons
        context.bot.send_photo(
            chat_id=update.message.chat_id,
            photo=WELCOME_IMAGE,
            caption="""
🌟 *Welcome to Fast Paisa Mini!* 🌟

✨ *Features:*
✅ Earn with daily tasks
🎁 Spin & win rewards
👥 Refer & earn $5 per friend
💰 Instant withdrawals

Click below to start earning!""",
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(keyboard)
            
    except Exception as e:
        logger.error(f"Error in start: {e}")

def main():
    updater = Updater(BOT_TOKEN, use_context=True)
    dp = updater.dispatcher
    
    dp.add_handler(CommandHandler("start", start))
    
    updater.start_polling()
    logger.info("Bot started successfully")
    updater.idle()

if __name__ == '__main__':
    main()
