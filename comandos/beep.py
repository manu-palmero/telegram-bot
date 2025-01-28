from telegram import *
from telegram.ext import *
import os

async def beep(update: Update, context: ContextTypes.DEFAULT_TYPE):
    frecuencia = context.args[0]
    tiempo = context.args[1]
    if not tiempo:
        await context.bot.send_message(update.effective_chat.id, f"No se especifico el tiempo")
    elif not frecuencia:
        await context.bot.send_message(update.effective_chat.id, f"No se especifico la frecuencia")
    else:
        os.system(f'beep -f {frecuencia} -l {tiempo}')
        await context.bot.send_message(update.effective_chat.id, f"Emitiendo un pitido de {frecuencia} Hz durante {tiempo/1000} segundos")

