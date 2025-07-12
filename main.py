import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

# Configure logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Your configuration
BOT_TOKEN = "7215344264:AAH_-h_D-DA_fZKPMLH98NQhAFRb_w3OF30"  # Replace with full token from BotFather
MINI_APP_URL = "https://cute-twilight-6eefd1.netlify.app"
WELCOME_IMAGE = "https://freeimage.host/i/FMntULN"  # Your provided image

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        user = update.effective_user
        
        # Create inline keyboard
        keyboard = [
            [InlineKeyboardButton("💰 Start Earning Now", web_app={"url": MINI_APP_URL})],
            [InlineKeyboardButton("📢 Join Channel", url="https://t.me/yourchannel")]
        ]
        
        # Send welcome message with features
        await context.bot.send_photo(
            chat_id=update.effective_chat.id,
            photo=WELCOME_IMAGE,
            caption=f"""
🌟 *Welcome {user.first_name} to Fast Paisa Mini!* 🌟

Here's what you can do:

🔄 *Daily Tasks* - Earn by completing simple tasks
🎡 *Spin & Win* - Try your luck daily for big rewards
👥 *Referral Program* - Get $5 for each friend who joins
📈 *Withdraw Easily* - Instant payments to your wallet

*Start earning in just 1 minute!*
            """,
            parse_mode="Markdown",
            reply_markup=InlineKeyboardMarkup(keyboard)
        )
        
    except Exception as e:
        logger.error(f"Error in start command: {e}")
        await update.message.reply_text("⚠️ Sorry, something went wrong. Please try again.")

async def handle_mini_app(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # This handles data if sent back from your mini app
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text="🎉 Welcome to Fast Paisa Mini App!")

def main():
    # Create application
    application = ApplicationBuilder().token(BOT_TOKEN).build()
    
    # Add handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(handle_mini_app))
    
    # Start the bot
    logger.info("Bot is starting...")
    application.run_polling()

if __name__ == "__main__":
    main()
