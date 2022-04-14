import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from domain.bot import BOT
from domain.user import User
from infrastructure.configuration import Config
from infrastructure.gpt3.gpt3_nlu import GPT3NLU

config = Config()
print("EJECUTANDO BOT EN MODO LOCAL")
print(f"TELEGRAM TOKEN {config.TELEGRAM_TOKEN}")
print(f"SERVICE STATUS {config.SERVICE_STATUS}")
print(f"IS SERVICE AVAILABLE {config.SERVICE_AVAILABLE}")

telegramBot = telegram.Bot(config.TELEGRAM_TOKEN)
nlu = GPT3NLU()
bot = BOT(nlu, config)


def init():
    updater = Updater(token=config.TELEGRAM_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), process_message))

    updater.start_polling()
    updater.idle()


def start(update: Update, context: CallbackContext):
    print("User connected")
    user = User(update.effective_chat.id, update.effective_chat.first_name)
    response = bot.handleStart(user)
    context.bot.send_message(chat_id=update.effective_chat.id, text=response.text)


def process_message(update: Update, context: CallbackContext):
    print(f"New message from {update.effective_user.first_name}, ${update.effective_chat.id}")
    text = update["message"]["text"]
    user = User(update.effective_chat.id, update.effective_chat.first_name)
    id = update.message.message_id
    date = str(update.message.date)
    response = bot.execute(text, user, id, date)
    print(text, response.text)
    context.bot.send_message(chat_id=update.effective_chat.id, text=response.text)


init()
