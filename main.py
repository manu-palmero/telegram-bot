from telegram.ext import *
from telegram import *

import funciones
from comandos import *

TOKEN = funciones.get_bot_token()


def main():
    application = Application.builder().token(TOKEN).build()

    add_cmds(application)

    application.run_polling()


def add_cmds(application):
    start_handler = CommandHandler('start', start.start)
    application.add_handler(start_handler)

    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo.echo)
    application.add_handler(echo_handler)

    temp_handler = CommandHandler('temp', temp.temp)
    application.add_handler(temp_handler)

    beep_handler = CommandHandler('beep', beep.beep)
    application.add_handler(beep_handler)
    
    botones_handler = CommandHandler('botones', prueba_botón.botones)
    application.add_handler(botones_handler)
    
    button_handler = CallbackQueryHandler(button.button)
    application.add_handler(button_handler)


if __name__ == '__main__':
    main()
