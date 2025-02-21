from telegram import *
from telegram.ext import *

async def botones(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [
            InlineKeyboardButton("Opción 1", callback_data='1'),
            InlineKeyboardButton("Opción 2", callback_data='2'),
        ],
        [InlineKeyboardButton("Opción 3", callback_data='3')],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text('Elige una opción:', reply_markup=reply_markup)
