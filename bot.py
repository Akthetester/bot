from telegram.ext import Application

TOKEN = "8699399335:AAHYf8Z60cpzJgVfkQ3ex4QzcaQIOzZnLHY"

app = Application.builder().token(TOKEN).build()

app.run_polling()
