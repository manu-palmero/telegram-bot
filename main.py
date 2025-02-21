from telegram.ext import *

import funciones
import comandos

TOKEN = funciones.get_bot_token()


def main():
    application = Application.builder().token(TOKEN).build()

    add_cmds(application)

    application.run_polling()


def add_cmds(application):
    start_handler = CommandHandler('start', comandos.start)
    application.add_handler(start_handler)

    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), comandos.echo)
    application.add_handler(echo_handler)

    temp_handler = CommandHandler('temp', comandos.temp)
    application.add_handler(temp_handler)

    beep_handler = CommandHandler('beep', comandos.beep)
    application.add_handler(beep_handler)
    
    botones_handler = CommandHandler('botones', comandos.botones)
    application.add_handler(botones_handler)
    
    button_handler = CallbackQueryHandler(comandos.button)
    application.add_handler(button_handler)


if __name__ == '__main__':
    main()
