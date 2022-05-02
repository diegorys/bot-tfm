import telegram
from conversational_bot.domain.client import Client
from sso.domain.user import User


class TelegramClient(Client):
    def __init__(self, token: str):
        self.telegramBot = telegram.Bot(token)

    def emit(self, user: User, text: str) -> None:
        telegramId = user.metadata["telegram_id"]
        self.telegramBot.send_message(chat_id=telegramId, text=text)
