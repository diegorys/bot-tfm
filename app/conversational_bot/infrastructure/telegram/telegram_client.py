import telegram
from conversational_bot.domain.client import Client
from sso.domain.user import User


class TelegramClient(Client):
    def __init__(self, token: str):
        self.telegramBot = telegram.Bot(token)

    def emit(self, user: User, text: str) -> None:
        telegramId = user.metadata["telegram_id"]
        if "1009284987" == telegramId:
            print(f"User: {user.username}")
            print(f"Telegram ID: {telegramId}")
            print(f"Text: {text}")
            print("-----")
            self.telegramBot.send_message(chat_id=telegramId, text=text)
