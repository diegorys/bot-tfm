from sso.domain.user import User


class UserExpression:
    def __init__(self, id, user: User, text, intent, entities, response, date=None):
        self.id = id
        self.user = User
        self.text = text
        self.intent = intent
        self.entities = entities.replace("'", "@")
        self.response = response
        self.date = date
