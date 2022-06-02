from random import randrange
from src.conversational_bot.frame import Frame
from src.conversational_bot.language_model import LanguageModel


class MockLanguageModel(LanguageModel):
    def identifyIntent(self, text: str) -> str:
        intent: str = "NO_IDENTIFICADO"
        return intent, {}

    def generateRequireParametersText(self, frame: Frame) -> str:
        response = ""
        for entity in frame.entities.keys():
            value = frame.entities[entity]
            if not value:
                response = f"required {entity}"
                break
        return response

    def generateText(self, frame: Frame) -> str:
        return frame.originalText
