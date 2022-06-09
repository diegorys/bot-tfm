import telegram
from src.conversational_bot.client import Client
from src.sso.domain.user import User


class TelegramClient(Client):
    def __init__(self, token: str):
        self.telegramBot = telegram.Bot(token)

    def emit(self, user: User, text: str) -> None:
        telegramId = ""
        if "telegram_id" in user.metadata.keys():
            telegramId = str(user.metadata["telegram_id"])
        # allowedUsers = ["1009284987"]
        if telegramId == "":
            print(f"El usuario {user.username} no tiene Telegram.")
        # elif telegramId in allowedUsers:
        else:
            print(f"User: {user.username}")
            print(f"Telegram ID: {telegramId}")
            print(f"Text: {text}")
            print("-----")
            self.telegramBot.send_message(chat_id=telegramId, text=text)
            print("sended!")
        # else:
        #     print(f"Usuario {telegramId} no permitido")
