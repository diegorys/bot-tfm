from conversational_bot.domain.frame import Frame


class LanguageModel:
    def identifyIntent(self, text: str):
        pass

    def generateText(self, frame: Frame) -> str:
        pass
