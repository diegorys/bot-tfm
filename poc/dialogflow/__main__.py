import os
import sys
from google.cloud import dialogflow
from google.protobuf.json_format import MessageToDict


GOOGLE_AUTHENTICATION_FILE_NAME = "./domain/key.json"
current_directory = os.path.dirname(os.path.realpath(__file__))
path = os.path.join(current_directory, GOOGLE_AUTHENTICATION_FILE_NAME)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = path

credentials = os.environ["GOOGLE_APPLICATION_CREDENTIALS"]
print(f"CREDENTIALS: {credentials}")


def detect_intent_texts(project_id, session_id, texts, language_code):
    """Returns the result of detect intent with texts as inputs.
    Using the same `session_id` between requests allows continuation
    of the conversation."""
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(project_id, session_id)
    print("Session path: {}\n".format(session))
    for text in texts:
        text_input = dialogflow.TextInput(text=text, language_code=language_code)
        query_input = dialogflow.QueryInput(text=text_input)
        response = session_client.detect_intent(
            request={"session": session, "query_input": query_input}
        )
        print("=" * 20)
        print("Query text: {}".format(response.query_result.query_text))
        print(
            "Detected intent: {} (confidence: {})\n".format(
                response.query_result.intent.display_name,
                response.query_result.intent_detection_confidence,
            )
        )
        print("Fulfillment text: {}\n".format(response.query_result.fulfillment_text))
        print(response)
        print('----------')
        print(response.query_result.fulfillment_messages[0].text.text[0])
        # print(response.query_result.parameters.values())
        notFounds = []
        for key, value in response.query_result.parameters.items():
            # json_obj = MessageToJson(value)
            # print(json_obj)
            print(key, value.value)
            if not value:
                notFounds.append(key)
        for key in response.query_result.parameters:
            print(key)
        print("Required")
        print(notFounds)
            


PROJECT_ID = "REPLACE_KEY"
SESSION = "123456789"
LANGUAGE_CODE = "es"


def execute():
    input_text = sys.argv[1]
    print(f"INPUT TEXT: {input_text}")
    detect_intent_texts(PROJECT_ID, SESSION, [input_text], LANGUAGE_CODE)


execute()
