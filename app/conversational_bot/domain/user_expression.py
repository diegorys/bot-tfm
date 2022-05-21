class UserExpression:
    def __init__(self, id, userid, username, text, intent, entities, response, date=None):
        self.id = id
        self.userid = userid
        self.username = username
        self.text = text
        self.intent = intent
        self.entities = entities.replace("'", "@")
        self.response = response
        self.date = date
