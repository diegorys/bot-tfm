import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from conversational_bot.use_cases.process_message_use_case import ProcessMessageUseCase
from sso.domain.user import User


class TelegramBot:
    def __init__(self, token: str, processMessageUseCase: ProcessMessageUseCase):
        self.token: str = token
        self.telegramBot = telegram.Bot(token)
        self.processMessageUseCase = processMessageUseCase

    def pool(self):
        updater = Updater(token=self.token, use_context=True)
        dispatcher = updater.dispatcher
        dispatcher.add_handler(CommandHandler("start", self.handleStartCommand))
        dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), self.handle))
        updater.start_polling()
        updater.idle()
        pass

    def handle(self, update: Update, context: CallbackContext) -> None:
        telegramId = update.effective_chat.id
        username = update.effective_chat.first_name
        id = update.message.message_id
        date = str(update.message.date)
        text = update["message"]["text"]
        user = User(
            update.effective_chat.first_name,
            {"telegram_id": update.effective_chat.id, "name": update.effective_chat.first_name},
        )
        print(f"> {telegramId} ({username}): {text}")
        response = self.processMessageUseCase.execute(user, text, date)
        print(f"< BOT: {response}")
        context.bot.send_message(chat_id=update.effective_chat.id, text=response)

    def handleStartCommand(self, update: Update, context: CallbackContext):
        print("User connected")
        # user = User(
        #     update.effective_chat.first_name,
        #     {
        #         "telegram_id": update.effective_chat.id,
        #     },
        # )
        # context.bot.send_message(chat_id=update.effective_chat.id, text=response.text)