import os

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from domain.user import User

class Handler:

  def __init__(self, token, logger, nlu):
    self.token = token
    self.logger = logger
    self.nlu = nlu
  
  def init(self):
    updater = Updater(token=self.token, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", self.start))
    dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), self.process_message))

    updater.start_polling()
    updater.idle()

  def start(self, update: Update, context: CallbackContext):
      self.logger.info("User connected")
      user = User(update.effective_chat.id, update.effective_chat.first_name)
      response = f'Hola {update.effective_user.first_name}'
      response = self.nlu.executeCommand(user, '/start')
      context.bot.send_message(
          chat_id=update.effective_chat.id, text=response
      )

  def process_message(self, update: Update, context: CallbackContext):
      self.logger.info(f'New message from {update.effective_user.first_name}, ${update.effective_chat.id}')
      text = update['message']['text']
      user = User(update.effective_chat.id, update.effective_chat.first_name)
      response = self.nlu.getResponse(user, text)
      context.bot.send_message(chat_id=update.effective_chat.id, text=response)