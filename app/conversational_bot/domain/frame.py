class Frame:
    def __init__(self, intent, user, originalText, entities={}):
        self.intent = intent
        self.user = user
        self.originalText = originalText
        self.entities = entities
