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
            realUser: User = user
            if realUser.isDependant() and not realUser.isMarkedAsActive():
                carevigne = realUser.relations["caregiver"]
                message = f"La persona a su cargo, {realUser.username} no responde."
                self.client.emit(carevigne, message)
            if realUser.isDependant() and not realUser.isActive():
                realUser.markActive(False)
                message = f"Hola {realUser.username}, hace un rato que no hablamos, ¿cómo estás?"
                self.client.emit(realUser, message)
            else:
                realUser.markActive(True)
