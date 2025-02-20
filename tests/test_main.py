import pytest
from telegram.ext import Application, CommandHandler, MessageHandler, filters
from main import add_cmds, main

def test_add_cmds():
    application = Application.builder().token("dummy_token").build()
    add_cmds(application)
    
    handlers = application.handlers[0]
    assert any(isinstance(handler, CommandHandler) and handler.command == ['start'] for handler in handlers)
    assert any(isinstance(handler, MessageHandler) and handler.filters == (filters.TEXT & (~filters.COMMAND)) for handler in handlers)
    assert any(isinstance(handler, CommandHandler) and handler.command == ['temp'] for handler in handlers)
    assert any(isinstance(handler, CommandHandler) and handler.command == ['beep'] for handler in handlers)

def test_main(mocker):
    mocker.patch('main.Application.builder', return_value=Application.builder().token("dummy_token").build())
    mocker.patch('main.add_cmds')
    mocker.patch('main.Application.run_polling')
    
    main()
    
    main.Application.builder.assert_called_once_with()
    main.add_cmds.assert_called_once()
    main.Application.run_polling.assert_called_once()
