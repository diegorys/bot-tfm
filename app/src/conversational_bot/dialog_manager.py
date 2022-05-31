from src.conversational_bot.response import Response
from src.conversational_bot.language_model import LanguageModel
from src.conversational_bot.frame import Frame


class DialogManager:
    def __init__(self, languageModel: LanguageModel):
        self.languageModel: LanguageModel = languageModel

    def execute(self, frame: Frame) -> Frame:        
        text: str = self.languageModel.generateRequireParametersText(frame)
        response: Response = Response(frame.user, text, frame.intent, frame.entities)
        return response
