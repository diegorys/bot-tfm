from datetime import datetime, timedelta
from src.events.domain.event import Event
from tests.sso.mothers.user_mother import UserMother


class EventMother:
    def getValid():
        user = UserMother.getValid()
        now = datetime.now().timestamp()
        event = Event(user, "DUMMY", {}, now)
        return event

    def withDelta(mins: int, hours: int = 0, days: int = 0):
        user = UserMother.getValid()
        now = (datetime.now() + timedelta(minutes=mins, hours=hours, days=days)).timestamp()
        event = Event(user, "DUMMY", {}, now)
        return event
