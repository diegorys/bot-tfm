from datetime import datetime, timedelta
from src.sso.domain.user import User
from src.conversational_bot.response import Response
from src.applications.status.domain.user_in_status_repository import UserInStatusRepository
from src.applications.status.domain.user_in_status import UserInStatus


class AskForUserStatusUseCase:
    def __init__(self, repository: UserInStatusRepository):
        self.repository = repository

    def execute(self, user: User):
        text: str = "No tienes a nadie a tu cuidado."
        response: Response = Response(user, text, "RESPONDER_ESTADO_PERSONA_MAYOR", {})
        if "dependents" in list(user.relations.keys()):
            text = ""
            for dependent in user.relations["dependents"]:
                userInStatus = self.repository.getStatusOf(dependent)
                dt_object = datetime.fromtimestamp(userInStatus.timestamp)
                date = (dt_object + timedelta(hours=2)).strftime("%d-%m-%Y a las %H:%M:%S")
                text += f"El estado de {userInStatus.user.username} el {date} era de {userInStatus.status.name}.\n"
        response.text = text.strip()
        return response
