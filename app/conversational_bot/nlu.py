from conversational_bot.language_model import LanguageModel
from conversational_bot.frame import Frame


class NLU:
    def __init__(self, languageModel: LanguageModel):
        self.languageModel: LanguageModel = languageModel

    def execute(self, user, text) -> Frame:
        intent, entities = self.languageModel.identifyIntent(text)
        frame: Frame = Frame(intent, user, text, entities)
        return frame
