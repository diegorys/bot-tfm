import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from src.conversational_bot.reactive_bot import ReactiveBOT
from src.sso.domain.user import User
from src.sso.domain.user_repository import UserRepository


class TelegramBot:
    def __init__(
        self,
        token: str,
        bot: ReactiveBOT,
        userRepository: UserRepository,
    ):
        self.token: str = token
        self.telegramBot = telegram.Bot(token)
        self.bot = bot
        self.userRepository = userRepository

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
        try:
            user = self.userRepository.getByMetadata("telegram_id", update.effective_chat.id)
            print(f"> {telegramId} ({username}): {text}")
            response = self.bot.execute(user, text, date)
            print(f"< BOT: {response.text}")
            context.bot.send_message(chat_id=update.effective_chat.id, text=response.text)
        except Exception as e:
            text = "Lo siento, no te conozco."
            print(e)
            context.bot.send_message(chat_id=update.effective_chat.id, text=text)

    def handleStartCommand(self, update: Update, context: CallbackContext):
        print("User connected")
