import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from conversational_bot.domain.client import Client
from sso.domain.user import User


class TelegramClient(Client):
    def __init__(self, token: str):
        self.token: str = token
        self.telegramBot = telegram.Bot(token)

    def pool(self):
        updater = Updater(token=self.token, use_context=True)
        dispatcher = updater.dispatcher
        dispatcher.add_handler(CommandHandler("start", self.start))
        dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), self.handle))
        updater.start_polling()
        updater.idle()
        pass

    def handle(self, text: str) -> None:
        pass

    def emit(self, text: str) -> None:
        pass

    def webhook(self, event) -> None:
        pass

    def start(self, update: Update, context: CallbackContext):
        print("User connected")
        # user = User(
        #     update.effective_chat.first_name,
        #     {
        #         "telegram_id": update.effective_chat.id,
        #     },
        # )
        # context.bot.send_message(chat_id=update.effective_chat.id, text=response.text)
