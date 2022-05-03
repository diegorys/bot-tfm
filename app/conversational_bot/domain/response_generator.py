from conversational_bot.domain.frame import Frame
from conversational_bot.domain.language_model import LanguageModel
from conversational_bot.domain.response import Response


class ResponseGenerator:
    def __init__(self, languageModel: LanguageModel):
        self.languageModel: LanguageModel = languageModel

    def execute(self, frame: Frame) -> Response:
        text: str = self.languageModel.generateText(frame)
        response: Response = Response(frame.user, text)
        response.intent = frame.intent
        return response
