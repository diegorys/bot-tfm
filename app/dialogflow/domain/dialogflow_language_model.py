from google.cloud import dialogflow
from conversational_bot.domain.frame import Frame
from conversational_bot.domain.language_model import LanguageModel


class DialogflowLanguageModel(LanguageModel):
    def __init__(self):
        pass

    def identifyIntent(self, text: str):
        pass

    def generateText(self, frame: Frame) -> str:
        pass
