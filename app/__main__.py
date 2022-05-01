import os
from conversational_bot.infrastructure.telegram.telegram_client import TelegramClient

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")

telegramClient: TelegramClient = TelegramClient(TELEGRAM_TOKEN)
telegramClient.pool()