from telegram import Update
from telegram.ext import ContextTypes


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    reply = ""
    for i in text:
        reply += f"{i} "
    await context.bot.send_message(chat_id=update.effective_chat.id, text=reply)
