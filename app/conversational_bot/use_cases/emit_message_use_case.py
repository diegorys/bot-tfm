from conversational_bot.domain.frame import Frame
from conversational_bot.domain.response_generator import ResponseGenerator
from sso.domain.user import User


class EmitMessageUseCase:
    def __init__(self, responseGenerator: ResponseGenerator):
        self.responseGenerator: ResponseGenerator = responseGenerator

    def execute(self, frame: Frame) -> None:
        self.responseGenerator.execute(frame)
