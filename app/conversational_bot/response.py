from sso.domain.user import User


class Response:
    def __init__(self, user: User, text: str):
        self.user = user
        self.text = text
