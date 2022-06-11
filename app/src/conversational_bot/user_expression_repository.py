from abc import abstractmethod
from src.conversational_bot.user_expression import UserExpression


class UserExpressionRepository:
    @abstractmethod
    def save(self, userExpression: UserExpression):
        pass

    @abstractmethod
    def list(self):
        pass
