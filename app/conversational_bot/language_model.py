from conversational_bot.frame import Frame


class LanguageModel:
    def identifyIntent(self, text: str):
        pass

    def generateRequireParametersText(self, frame: Frame) -> str:
        pass

    def generateText(self, frame: Frame) -> str:
        pass
