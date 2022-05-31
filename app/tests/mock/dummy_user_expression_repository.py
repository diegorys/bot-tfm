from sso.domain.user import User
from conversational_bot.user_expression_repository import UserExpressionRepository
from conversational_bot.user_expression_repository import UserExpression


class DummyUsersExpressionRepository(UserExpressionRepository):
    def save(self, userExpression: UserExpression):
        return userExpression
