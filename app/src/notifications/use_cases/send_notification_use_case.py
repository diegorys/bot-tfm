from src.conversational_bot.response_generator import ResponseGenerator
from src.conversational_bot.frame import Frame
from src.conversational_bot.client import Client
from src.sso.domain.user_repository import UserRepository


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
