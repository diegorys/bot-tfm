import os

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from domain.user import User
from domain.knowledge import Knowledge


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
        self.log("", response)
        context.bot.send_message(chat_id=update.effective_chat.id, text=response.text)

    def process_message(self, update: Update, context: CallbackContext):
        self.logger.info(
            f"New message from {update.effective_user.first_name}, ${update.effective_chat.id}"
        )
        text = update["message"]["text"]
        user = User(update.effective_chat.id, update.effective_chat.first_name)
        response = self.nlu.getResponse(user, text)
        self.log(text, response)
        context.bot.send_message(chat_id=update.effective_chat.id, text=response.text)

    def log(self, request, response):
        text = (
            str(response.user.id)
            + "|"
            + response.user.name
            + "|"
            + response.domain
            + "|"
            + response.intent
            + "|"
            + str(response.probability)
            + "|"
            + request
            + "|"
            + response.text
            + "|"
            + response.command
            + "\n"
        )
        knowledge = Knowledge(
            request, response.domain, response.intent, response.command, response.text
        )
        self.knowledgeRepository.save(knowledge)
        print(text)
        f = open("/logs/log.txt", "a")
        f.write(text)
        f.close()
