from conversational_bot.domain.frame import Frame
from conversational_bot.domain.response import Response
from conversational_bot.domain.response_generator import ResponseGenerator

"""
A partir de un texto, genera una respuesta y procesa el comando.
"""


class ProactiveBOT:
    def __init__(
        self,
        responseGenerator: ResponseGenerator,
    ):
        self.responseGenerator: ResponseGenerator = responseGenerator

    def generate(self, frame: Frame) -> Response:
        response = self.responseGenerator.execute(frame)
        return response
