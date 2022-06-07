from datetime import datetime
from src.sso.domain.user import User
from src.sso.domain.user_repository import UserRepository
from src.conversational_bot.client import Client


class AlertOfInactivityUseCase:
    def __init__(self, userRepository: UserRepository, client: Client):
        self.userRepository = userRepository
        self.client = client

    def execute(self):
        users = self.userRepository.list()
        for user in users:
            dependent: User = user
            if "caregiver" in dependent.relations.keys() and not dependent.isMarkedAsActive():
                carevigne = dependent.relations["caregiver"]
                message = f"La persona a su cargo, {dependent.username} no responde."
                self.client.emit(carevigne, message)
