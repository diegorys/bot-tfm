from conversational_bot.domain.client import Client
from conversational_bot.domain.frame import Frame
from conversational_bot.domain.language_model import LanguageModel


class ResponseGenerator:
    def __init__(self, client: Client, languageModel: LanguageModel):
        self.client: Client = client
        self.languageModel: LanguageModel = languageModel

    def execute(self, frame: Frame) -> None:
        text: str = self.languageModel.generateText(frame)
        print(f"Language model generated {text}")
        self.client.emit(text)
