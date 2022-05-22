import time
from conversational_bot.command_manager import CommandManager
from conversational_bot.dialog_manager import DialogManager
from conversational_bot.frame import Frame
from conversational_bot.nlu import NLU
from conversational_bot.response import Response
from conversational_bot.response_generator import ResponseGenerator
from conversational_bot.user_expression import UserExpression
from conversational_bot.user_expression_repository import UserExpressionRepository
from sso.domain.user import User

"""
A partir de un texto, genera una respuesta y procesa el comando.
"""


class ReactiveBOT:
    def __init__(
        self,
        nlu: NLU,
        dialogManager: DialogManager,
        responseGenerator: ResponseGenerator,
        commandManager: CommandManager,
        userExpressionRepository: UserExpressionRepository
    ):
        self.nlu: NLU = nlu
        self.dialogManager = dialogManager
        self.responseGenerator: ResponseGenerator = responseGenerator
        self.commandManager = commandManager
        self.userExpressionRepository = userExpressionRepository

    def execute(self, user: User, text: str, date) -> Response:
        frame: Frame = self.nlu.execute(user, text)
        if frame.isComplete():
            response = self.responseGenerator.execute(frame)
            self.commandManager.execute(frame)
            now = str(time.time())
            userExpression = UserExpression(
                now,
                user,
                text,
                response.intent,
                response.entities,
                response.text,
                date,
            )
            self.userExpressionRepository.save(userExpression)
        else:
            response = self.dialogManager.execute(frame)
        return response
