import os
import logging

from infrastructure.gpt3.gpt3 import GPT3
from infrastructure.telegram.handler import Handler
from actions.default import Default
from actions.say_hello import SayHello
from actions.introduce_oneself import IntroduceOnself
from actions.remember_medicine import RememberMedicine

print("BOT STARTING")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)

TOKEN = os.getenv("TELEGRAM_TOKEN")
print(TOKEN)
nlu = GPT3()
nlu.handle(Default('DEFAULT'))
nlu.handle(SayHello('SALUDAR'))
nlu.handle(RememberMedicine('RECORDAR_MEDICINA'))
nlu.handle(IntroduceOnself('/start'))
handler = Handler(TOKEN, logger, nlu)
handler.init()