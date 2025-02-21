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
        return
    finally:
        try:
            tiempo = context.args[1]
        except IndexError:
            await context.bot.send_message(update.effective_chat.id, f"No se especificó el tiempo")
            print(f"No se especificó el tiempo")
            return
        else:
            s = float(tiempo)/1000
            await context.bot.send_message(update.effective_chat.id, f"Emitiendo un pitido de {frecuencia} Hz durante {s} segundos")
            
            try:
                os.system(f'beep -f {frecuencia} -l {tiempo}')
            except Exception as e:
                await context.bot.send_message(update.effective_chat.id, f"Error al emitir el pitido: {e}")
                print(f"Error al emitir el pitido: {e}")
            else:
                await context.bot.send_message(update.effective_chat.id, f"Se terminó de emitir el pitido de {frecuencia} Hz")