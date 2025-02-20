import pytest
from unittest.mock import AsyncMock, patch
from telegram import Update
from telegram.ext import ContextTypes
from comandos.beep import beep


@pytest.mark.asyncio
async def test_beep_no_frecuencia():
    update = Update(update_id=1, message=AsyncMock())
    context = AsyncMock()
    context.args = []

    await beep(update, context)

    context.bot.send_message.assert_called_once_with(
        update.effective_chat.id, "No se especificó la frecuencia"
    )


@pytest.mark.asyncio
async def test_beep_no_tiempo():
    update = Update(update_id=1, message=AsyncMock())
    context = AsyncMock()
    context.args = ["440"]

    await beep(update, context)

    context.bot.send_message.assert_called_once_with(
        update.effective_chat.id, "No se especificó el tiempo"
    )


@pytest.mark.asyncio
@patch("os.system")
async def test_beep_correct_args(mock_os_system):
    update = Update(update_id=1, message=AsyncMock())
    context = AsyncMock()
    context.args = ["440", "1000"]

    await beep(update, context)

    s = float(context.args[1]) / 1000
    context.bot.send_message.assert_any_call(
        update.effective_chat.id,
        f"Emitiendo un pitido de {context.args[0]} Hz durante {s} segundos",
    )
    mock_os_system.assert_called_once_with(
        f"beep -f {context.args[0]} -l {context.args[1]}"
    )
    context.bot.send_message.assert_any_call(
        update.effective_chat.id,
        f"Se terminó de emitir el pitido de {context.args[0]} Hz",
    )
