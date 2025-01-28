from telegram import *
from telegram.ext import *
import os

async def beep(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("context.args: ",context.args)
    print("len context.args: ",len(context.args))
    try:
        frecuencia = context.args[0]
    except IndexError:
        await context.bot.send_message(update.effective_chat.id, f"No se especificó la frecuencia")
        print(f"No se especificó la frecuencia")
    try:
        tiempo = context.args[1]
    except IndexError:
        await context.bot.send_message(update.effective_chat.id, f"No se especificó el tiempo")

        os.system(f'beep -f {frecuencia} -l {tiempo}')
        await context.bot.send_message(update.effective_chat.id, f"Emitiendo un pitido de {frecuencia} Hz durante {tiempo/1000} segundos")

