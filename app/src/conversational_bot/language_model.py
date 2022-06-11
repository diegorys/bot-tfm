from abc import abstractmethod
from src.conversational_bot.frame import Frame


class LanguageModel:
    @abstractmethod
    def identifyIntent(self, text: str):
        pass

    @abstractmethod
    def generateRequireParametersText(self, frame: Frame) -> str:
        pass

    @abstractmethod
    def generateText(self, frame: Frame) -> str:
        pass
