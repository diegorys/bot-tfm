from pickle import NONE
import time
from uuid import uuid4
from src.sso.domain.user import User


class Event:
    def __init__(self, user: User, intent: str, entities, timestamp: float, id: str = None):
        if type(user) is not User:
            raise Exception(
                f"""Arg user must be an object of User class.
                Getted class {type(user)}"""
            )
        if type(intent) is not str:
            raise Exception(
                f"""Arg intent must be an object of User class.
                Getted class {type(intent)}"""
            )
        if type(timestamp) is not float:
            raise Exception(
                f"""Arg timestamp must be an object of User class.
                Getted class {type(timestamp)}"""
            )
        self.id = id
        if self.id is None:
            self.id = str(uuid4())
        self.user = user
        self.intent = intent
        self.entities = entities
        self.timestamp = timestamp

    def hasExpired(self, timestamp: float) -> bool:
        print(f"{self.id} - ${self.timestamp} - ${timestamp}")
        return self.timestamp < timestamp
