import os
from typing import Dict
from google.cloud import dialogflow
from google.protobuf.json_format import MessageToDict
from src.conversational_bot.frame import Frame
from src.conversational_bot.language_model import LanguageModel


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
        session = session_client.session_path(PROJECT_ID, SESSION)
        text_input = dialogflow.TextInput(text=text, language_code=LANGUAGE_CODE)
        query_input = dialogflow.QueryInput(text=text_input)
        response = session_client.detect_intent(
            request={"session": session, "query_input": query_input}
        )
        response_json = MessageToDict(
            response._pb
        )  # TODO: hay más parámetros interesantes, como si están todos los campos requeridos o la "confidencia".
        intent = response_json["queryResult"]["intent"]["displayName"]
        parameters = response_json["queryResult"]["parameters"]
        entities = {}
        for entityName in parameters.keys():
            if entityName == "date-time":
                entities["cuando"] = self.parseDateTime(parameters["date-time"])
            elif len(parameters[entityName]) > 0:
                entities[entityName] = parameters[entityName][0]
            else:
                entities[entityName] = ""
        self.lastResponse = response.query_result.fulfillment_messages[0].text.text[
            0
        ]
        self.lastResponse = self.lastResponse.replace("date-time", "cuándo")
        return intent, entities

    def generateRequireParametersText(self, frame: Frame) -> str:
        return self.lastResponse

    def generateText(self, frame: Frame) -> str:
        return self.lastResponse

    def parseDateTime(self, dateTime):
        cuando = ""
        print(dateTime)
        if len(dateTime) > 0:
            e = dateTime[0]
            if type(e) is dict:
                if "date_time" in e.keys():
                    cuando = e["date_time"]
                elif "endDateTime" in e.keys():
                    cuando = e["endDateTime"]
                elif "endDate" in e.keys():
                    cuando = e["endDate"]
                elif "endTime" in e.keys():
                    cuando = e["endTime"]
            else:
                cuando = e
        print("cuando")
        print(cuando)
        return cuando

