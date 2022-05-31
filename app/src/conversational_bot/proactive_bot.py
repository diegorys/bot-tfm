from src.conversational_bot.client import Client
from src.conversational_bot.frame import Frame
from src.conversational_bot.response import Response
from src.conversational_bot.response_generator import ResponseGenerator

"""
A partir de un texto, genera una respuesta y procesa el comando.
"""


class ProactiveBOT:
    def __init__(self, responseGenerator: ResponseGenerator, client: Client):
        self.responseGenerator: ResponseGenerator = responseGenerator
        self.client = client

    def execute(self, frame: Frame) -> Response:
        response = self.responseGenerator.execute(frame)
        self.client.emit(frame.user, response.text)

