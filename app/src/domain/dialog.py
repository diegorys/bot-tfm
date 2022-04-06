class Dialog:
    def __init__(self, userid, username, text, domain, intent, entities, response, date=None):
        self.userid = (userid,)
        self.username = (username,)
        self.text = text
        self.domain = domain
        self.intent = intent
        self.entities = entities.replace("'", "@")
        self.response = response
        self.date = date
