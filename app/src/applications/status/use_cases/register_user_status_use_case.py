from src.conversational_bot.client import Client
from src.applications.status.domain.user_in_status_repository import UserInStatusRepository
from src.applications.status.domain.user_in_status import UserInStatus


class RegisterUserStatusUseCase:
    def __init__(self, repository: UserInStatusRepository, client: Client):
        self.blackList = ["tristeza", "soledad", "cansancio", "muy triste"]
        self.repository = repository
        self.client = client

    def execute(self, userInStatus: UserInStatus):
        saved = self.repository.save(userInStatus)
        if userInStatus.status.name in self.blackList and userInStatus.user.isDependant():
            caregiver = userInStatus.user.getCaregiver()
            message = f"Hola {caregiver.username}, el estado de la persona a la que cuidas, {userInStatus.user.username} es de {userInStatus.status.name}"
            print(message)
            self.client.emit(caregiver, message)
        return saved
