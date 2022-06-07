from datetime import datetime
from src.sso.domain.user import User


class MarkASInactiveUseCase:
    # Execute at 13:00 and at 20:00. Checks 3 hours of inactivity.
    def execute(self, user: User):
        timestampLastActivity: float = float(user.metadata["last_activity"])
        timestampNow: float = datetime.now().timestamp()
        pass
