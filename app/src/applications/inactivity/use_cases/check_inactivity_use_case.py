from datetime import datetime
from src.sso.domain.user_repository import UserRepository
from src.sso.domain.user import User
from src.conversational_bot.client import Client


class CheckInactivityUseCase:
    def __init__(self, userRepository: UserRepository, client: Client):
        self.userRepository = userRepository
        self.client = client

    def execute(self):
        print(f"[CheckInactivityUseCase][execute]")
        users = self.userRepository.list()
        for user in users:
            realUser: User = user
            print(f"[CheckInactivityUseCase][execute]: {realUser.id}: {realUser.username}")
            if realUser.isDependant() and not realUser.isMarkedAsActive():
                carevigne = realUser.relations["caregiver"]
                message = f"La persona a su cargo, {realUser.username}, no responde."
                print(message)
                self.client.emit(carevigne, message)
            elif realUser.isDependant() and not realUser.isActive():
                realUser.markActive(False)
                self.userRepository.save(realUser)
                message = f"Hola {realUser.username}, hace un rato que no hablamos, ¿cómo estás?"
                print(message)
                self.client.emit(realUser, message)
            else:
                message = f"Usuario {realUser.username} activo"
                realUser.markActive(True)
                self.userRepository.save(realUser)
                print(message)
