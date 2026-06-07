from telegram.ext import Application, CommandHandler
import os

TOKEN = os.getenv("8699399335:AAHYf8Z60cpzJgVfkQ3ex4QzcaQIOzZnLHY")

async def start(update, context):
    await update.message.reply_text("Bot is running!")

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

print("Bot Started...")
app.run_polling()
