import os

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from domain.user import User


class Handler:
    def __init__(self, token, logger, nlu, knowledgeRepository):
        self.token = token
        self.logger = logger
        self.nlu = nlu
        self.knowledgeRepository = knowledgeRepository

    def init(self):
        updater = Updater(token=self.token, use_context=True)
        dispatcher = updater.dispatcher

        dispatcher.add_handler(CommandHandler("start", self.start))
        dispatcher.add_handler(
            MessageHandler(Filters.text & (~Filters.command), self.process_message)
        )

        updater.start_polling()
        updater.idle()

    def start(self, update: Update, context: CallbackContext):
        self.logger.info("User connected")
        user = User(update.effective_chat.id, update.effective_chat.first_name)
        response = f"Hola {update.effective_user.first_name}"
        response = self.nlu.executeCommand(user, "/start")
        self.log(user, "/start", "", 100, "", response)
        context.bot.send_message(chat_id=update.effective_chat.id, text=response)

    def process_message(self, update: Update, context: CallbackContext):
        self.logger.info(
            f"New message from {update.effective_user.first_name}, ${update.effective_chat.id}"
        )
        text = update["message"]["text"]
        user = User(update.effective_chat.id, update.effective_chat.first_name)
        domain, intent, p, response = self.nlu.getResponse(user, text)
        self.log(user, domain, intent, p, text, response)
        # status = self.nlu.identifyEmotion(user, text)
        # self.log(user, 'emotion', status['probability'], text, status['log'])
        context.bot.send_message(chat_id=update.effective_chat.id, text=response)
        # context.bot.send_message(chat_id=update.effective_chat.id, text=status['response'])

    def log(self, user, domain, intent, p, request, response):
        text = (
            str(user.id)
            + "|"
            + user.name
            + "|"
            + domain
            + "|"
            + intent
            + "|"
            + str(p)
            + "|"
            + request
            + "|"
            + response
            + "\n"
        )
        print(text)
        f = open("/logs/log.txt", "a")
        f.write(text)
        f.close()
