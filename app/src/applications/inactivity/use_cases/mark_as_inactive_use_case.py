from datetime import datetime
from src.sso.domain.user_repository import UserRepository
from src.sso.domain.user import User
from src.conversational_bot.client import Client


class MarkASInactiveUseCase:
    def __init__(self, userRepository: UserRepository, client: Client):
        self.userRepository = userRepository
        self.client = client

    # Execute at 13:00 and at 20:00. Checks 3 hours of inactivity.
    def execute(self):
        users = self.userRepository.list()
        for user in users:
            dependent: User = user
            # if "caregiver" in dependent.relations.keys() and not dependent.isMarkedAsActive():
            #     carevigne = dependent.relations["caregiver"]
            #     message = f"La persona a su cargo, {dependent.username} no responde."
            #     self.client.emit(carevigne, message)
            if dependent.isDependant() and not dependent.isActive():
                dependent.markActive(False)
                message = f"Hola {dependent.username}, hace un rato que no hablamos, ¿cómo estás?"
                self.client.emit(dependent, message)
            else:
                dependent.markActive(True)
