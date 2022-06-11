from src.conversational_bot.language_model import LanguageModel
from tests.conversational_bot.mother.frame_mother import FrameMother

def test_language_model_identify_intent():
    lm = LanguageModel()

    lm.identifyIntent("a")

    assert type(lm) == LanguageModel

def test_language_model_identify_intent():
    lm = LanguageModel()

    frame = FrameMother.getValid()
    response = lm.generateRequireParametersText(frame)

    assert type(lm) == LanguageModel

def test_language_model_identify_intent():
    lm = LanguageModel()

    frame = FrameMother.getValid()
    lm.generateText(frame)

    assert type(lm) == LanguageModel

