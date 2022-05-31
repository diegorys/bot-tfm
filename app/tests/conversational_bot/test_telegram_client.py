import os
import pytest
from interfaces.telegram_client import TelegramClient

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")


def test_construct():
    TelegramClient(TELEGRAM_TOKEN)


def test_construct_error():
    with pytest.raises(Exception):
        TelegramClient("abcd")


def test_start():
    telegramClient: TelegramClient = TelegramClient(TELEGRAM_TOKEN)
    # telegramClient.start()


def test_handle():
    telegramClient: TelegramClient = TelegramClient(TELEGRAM_TOKEN)
    # telegramClient.handle("Hola robot")


def test_emit():
    telegramClient: TelegramClient = TelegramClient(TELEGRAM_TOKEN)
    # telegramClient.emit("Hola robot", None)
