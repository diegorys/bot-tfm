import os
import logging

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from infrastructure.telegram.handler import Handler

print("BOT STARTING")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)

TOKEN = os.getenv("OPENAI_API_KEY")
handler = Handler(TOKEN, logger)
handler.init()