import os
import logging
from domain.knowledge import Knowledge

from infrastructure.gpt3.gpt3_nlu import GPT3NLU
from infrastructure.telegram.handler import Handler
from infrastructure.sqlite3.sqlite3_knowledge_repository import SQLite3KnowledgeRepository
from actions.default import Default
from actions.introduce_oneself import IntroduceOnself
from actions.register_medicine import RegisterMedicine
from actions.register_status import RegisterStatus
from actions.say_hello import SayHello

TOKEN = os.getenv("TELEGRAM_TOKEN")

print("BOT STARTING")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)

knowledgeRepository = SQLite3KnowledgeRepository("bot-tfm")
nlu = GPT3NLU()
nlu.handle(Default("DESCONOCIDA"))
nlu.handle(SayHello("SALUDAR"))
nlu.handle(RegisterMedicine("REGISTRAR_MEDICACION"))
nlu.handle(RegisterStatus("REGISTRAR_ESTADO"))
nlu.handle(IntroduceOnself("/start"))
handler = Handler(TOKEN, logger, nlu, knowledgeRepository)
handler.init()
