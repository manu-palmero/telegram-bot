from telegram import *
from telegram.ext import *

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    
    respuestas = {
        "1": "Has elegido la Opción 1",
        "2": "Has elegido la Opción 2",
        "3": "Has elegido la Opción 3",
    }
    
    await query.edit_message_text(text=respuestas.get(query.data, "Opción no válida"))
