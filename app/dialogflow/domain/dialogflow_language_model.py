import os
from google.cloud import dialogflow
from conversational_bot.domain.frame import Frame
from conversational_bot.domain.language_model import LanguageModel

PROJECT_ID = "***REMOVED***"
SESSION = "123456789"
LANGUAGE_CODE = "es"

GOOGLE_AUTHENTICATION_FILE_NAME = "key.json"
current_directory = os.path.dirname(os.path.realpath(__file__))
path = os.path.join(current_directory, GOOGLE_AUTHENTICATION_FILE_NAME)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = path


class DialogflowLanguageModel(LanguageModel):
    def __init__(self):
        self.lastResponse = ""

    def identifyIntent(self, text: str):
        session_client = dialogflow.SessionsClient()
        session = session_client.session_path(PROJECT_ID, 123456789)
        text_input = dialogflow.TextInput(text=text, language_code=LANGUAGE_CODE)
        query_input = dialogflow.QueryInput(text=text_input)
        response = session_client.detect_intent(
            request={"session": session, "query_input": query_input}
        )
        intent = response.query_result.intent.display_name
        # parameters = response.query_result.parameters.fields
        entities = {}
        self.lastResponse = response.query_result.fulfillment_messages[0].text.text[0]
        return intent, entities

    def generateText(self, frame: Frame) -> str:
        return self.lastResponse
