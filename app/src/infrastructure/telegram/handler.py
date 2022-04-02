import os

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

class Handler:

  def __init__(self, token, logger):
    self.token = token
    self.logger = logger
  
  def init(self):
    updater = Updater(token=self.token, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", self.start))
    dispatcher.add_handler(MessageHandler(Filters.text & (~Filters.command), self.process_message))

    updater.start_polling()
    updater.idle()

  def start(self, update: Update, context: CallbackContext):
      self.logger.info("User connected")
      response = f'Hola {update.effective_user.first_name}'
      context.bot.send_message(
          chat_id=update.effective_chat.id, text=response
      )

  def process_message(self, update: Update, context: CallbackContext):
      self.logger.info(f'New message from {update.effective_user.first_name}, ${update.effective_chat.id}')
      context.bot.send_message(chat_id=update.effective_chat.id, text="No te entiendo")