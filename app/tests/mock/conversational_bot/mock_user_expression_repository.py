from src.sso.domain.user import User
from src.conversational_bot.user_expression_repository import UserExpressionRepository
from src.conversational_bot.user_expression_repository import UserExpression


class MockUsersExpressionRepository(UserExpressionRepository):
    def save(self, userExpression: UserExpression):
        return userExpression
