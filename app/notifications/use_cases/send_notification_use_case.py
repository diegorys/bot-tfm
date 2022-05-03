from conversational_bot.domain.response_generator import ResponseGenerator
from conversational_bot.domain.frame import Frame
from conversational_bot.domain.client import Client
from sso.domain.user_repository import UserRepository


class SendNotificationUseCase:
    def __init__(
        self, client: Client, responseGenerator: ResponseGenerator, usersRepository: UserRepository
    ):
        self.client = client
        self.responseGenerator = responseGenerator
        self.usersRepository = usersRepository

    def execute(self, notification):
        users = self.usersRepository.list()
        for user in users:
            frame = Frame("NOTIFICATION", user, "", notification)
            response = self.responseGenerator.execute(frame)
            self.client.emit(frame.user, response.text)
