import os
import logging
from domain.knowledge import Knowledge

from infrastructure.gpt3.gpt3 import GPT3
from infrastructure.telegram.handler import Handler
from infrastructure.sqlite3.sqlite3_knowledge_repository import SQLite3KnowledgeRepository
from actions.default import Default
from actions.say_hello import SayHello
from actions.introduce_oneself import IntroduceOnself
from actions.remember_medicine import RememberMedicine

print("BOT STARTING")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logger = logging.getLogger(__name__)
knowledgeRepository = SQLite3KnowledgeRepository("bot-tfm")
knowledgeRepository.truncate()
knowledges = [
    Knowledge("Hola", "SALUDAR", "DECIR_HOLA", "emisor={USUARIO_NOMBRE}", "Hola ${emisor)"),
    Knowledge("Estoy triste", "ESTADO", "IDENTIFICAR", "estado=triste", "Tranquilo"),
    Knowledge("Me siento bien", "ESTADO", "IDENTIFICAR", "estado=bien", "Veo que estás ${estado}, Me alegro"),
    Knowledge("Me siento solo", "ESTADO", "IDENTIFICAR", "estado=solo", "Sientes ${estado}, yo te acompaño"),
    Knowledge("Me siento solo", "ESTADO", "IDENTIFICAR", "estado=solo", "Sientes ${estado}, yo te acompaño"),
    Knowledge("Me siento solo", "ESTADO", "IDENTIFICAR", "estado=solo", "Sientes ${estado}, yo te acompaño"),
    Knowledge("Me siento solo", "ESTADO", "IDENTIFICAR", "estado=solo", "Sientes ${estado}, yo te acompaño"),
    Knowledge("Me siento solo", "ESTADO", "IDENTIFICAR", "estado=solo", "Sientes ${estado}, yo te acompaño"),
    Knowledge("Me siento solo", "ESTADO", "IDENTIFICAR", "estado=solo", "Sientes ${estado}, yo te acompaño"),
    Knowledge("Me siento solo", "ESTADO", "IDENTIFICAR", "estado=solo", "Sientes ${estado}, yo te acompaño"),
    Knowledge(
        "Tengo que tomar un ibuprofeno los lunes",
        "MEDICACION",
        "RECORDAR_MEDICINA",
        "medicina=ibuprofeno;cuando=lunes",
        "Vale, el ibuprofeno los lunes",
    ),
    Knowledge(
        "A las 12:00 me toca el paracetamol",
        "MEDICACION",
        "RECORDAR_MEDICINA",
        "medicina=paracetamol;cuando=12:00",
        "De acuerdo, a las 12:00 te tienes que tomar el paracetamol",
    ),
]

for knowledge in knowledges:
    knowledgeRepository.save(knowledge)

TOKEN = os.getenv("TELEGRAM_TOKEN")
print(TOKEN)
nlu = GPT3(knowledgeRepository)
nlu.handle(Default("DEFAULT"))
nlu.handle(SayHello("SALUDAR"))
nlu.handle(RememberMedicine("RECORDAR_MEDICINA"))
nlu.handle(IntroduceOnself("/start"))
handler = Handler(TOKEN, logger, nlu, knowledgeRepository)
handler.init()
