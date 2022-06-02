from src.conversational_bot.dialog_manager import DialogManager
from src.conversational_bot.response import Response
from tests.conversational_bot.mocks.mock_language_model import MockLanguageModel
from tests.conversational_bot.mother.frame_mother import FrameMother


def test_execute():
  languageModel = MockLanguageModel()
  dialogManager = DialogManager(languageModel)
  frame = FrameMother.getValid()
  expected:Response = Response(frame.user, "", frame.intent, frame.entities)
  
  received: Response = dialogManager.execute(frame)

  assert received.intent == expected.intent
  assert received.text == expected.text