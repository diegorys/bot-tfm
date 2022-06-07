from datetime import datetime
from sso.domain.user import User
from sso.domain.user_repository import UserRepository


class AlertOfInactivityUseCase:
    def __init__(self, userRepository: UserRepository):
        self.userRepository = userRepository

    def execute(self):
        users = self.userRepository.list()        
        for user in users:
            userC: User = user
            if userC.metadata["inactive"]:
                carevigne = userC.relations[""]
                print(f"El usuario {userC.username} está inactivo. Avisar a su cuidador {carevigne}")
