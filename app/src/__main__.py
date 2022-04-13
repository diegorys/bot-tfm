import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from infrastructure.configuration import Config

config = Config()
print('EJECUTANDO BOT EN MODO LOCAL')
print(f"TELEGRAM TOKEN {config.TELEGRAM_TOKEN}")
print(f"SERVICE STATUS {config.SERVICE_STATUS}")
print(f"IS SERVICE AVAILABLE {config.SERVICE_AVAILABLE}")

bot = telegram.Bot(config.TELEGRAM_TOKEN)

def init():
    updater = Updater(token=config.TELEGRAM_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(
        MessageHandler(Filters.text & (~Filters.command), process_message)
    )

    updater.start_polling()
    updater.idle()

def start(update: Update, context: CallbackContext):
    print("User connected")
    context.bot.send_message(chat_id=update.effective_chat.id, text='HOLA!!!')

def process_message(update: Update, context: CallbackContext):
    print(
        f"New message from {update.effective_user.first_name}, ${update.effective_chat.id}"
    )
    text = update["message"]["text"]
    response = f"Me has dicho {text}"
    print(text, response)
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)

init()