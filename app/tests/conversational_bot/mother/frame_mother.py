from src.conversational_bot.frame import Frame
from tests.sso.mothers.user_mother import UserMother


class FrameMother:
    def getValid():
        user = UserMother.getValid()
        return Frame("intenttest", user, "text")
