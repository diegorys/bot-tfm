import os
import logging

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from infrastructure.telegram.handler import Handler
from domain.nlu import NLU

print("BOT STARTING")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)

TOKEN = os.getenv("TELEGRAM_TOKEN")
handler = Handler(TOKEN, logger, NLU)
handler.init()