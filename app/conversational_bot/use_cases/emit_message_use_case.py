from conversational_bot.domain.client import Client
from conversational_bot.domain.frame import Frame
from conversational_bot.domain.response_generator import ResponseGenerator
from sso.domain.user import User


class EmitMessageUseCase:
    def __init__(self, client: Client, responseGenerator: ResponseGenerator):
        self.client = client
        self.responseGenerator: ResponseGenerator = responseGenerator

    def execute(self, user: User, frame: Frame) -> None:
        response = self.responseGenerator.execute(frame)
        self.client.emit(response)

