from telegram import Update
from telegram.ext import ContextTypes

import funciones


async def temp(update: Update, context: ContextTypes.DEFAULT_TYPE):
    t = funciones.temperatura()
    text = f"La temperatura es: {t}°C"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text)
