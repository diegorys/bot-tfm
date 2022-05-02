from conversational_bot.domain.response_generator import ResponseGenerator
from conversational_bot.domain.frame import Frame
from conversational_bot.domain.client import Client
from sso.domain.user import User


class SendNotificationUseCase:
    def __init__(self, client: Client, responseGenerator: ResponseGenerator):
        self.client = client
        self.responseGenerator = responseGenerator

    def execute(self, frame: Frame):
        response = self.responseGenerator.execute(frame)
        self.client.emit(frame.user, response)
