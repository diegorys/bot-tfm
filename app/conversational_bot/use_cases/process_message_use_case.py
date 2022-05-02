from conversational_bot.domain.frame import Frame
from conversational_bot.domain.nlu import NLU
from conversational_bot.domain.response_generator import ResponseGenerator
from sso.domain.user import User


class ProcessMessageUseCase:
    def __init__(self, nlu: NLU, responseGenerator: ResponseGenerator):
        self.nlu: NLU = nlu
        self.responseGenerator: ResponseGenerator = responseGenerator

    def execute(self, user: User, text: str, date) -> None:
        print(f"Text: {text}")
        frame: Frame = self.nlu.execute(user, text)
        response = self.responseGenerator.execute(frame)
        return response
