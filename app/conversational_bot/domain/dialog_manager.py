from conversational_bot.domain.response import Response
from conversational_bot.domain.language_model import LanguageModel
from conversational_bot.domain.frame import Frame


class DialogManager:
    def __init__(self, languageModel: LanguageModel):
        self.languageModel: LanguageModel = languageModel

    def execute(self, frame: Frame) -> Frame:
        text: str = self.languageModel.generateRequireParametersText(frame)
        response: Response = Response(frame.user, text)
        response.intent = frame.intent
        return response
