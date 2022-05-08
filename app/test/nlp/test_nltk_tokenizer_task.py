import pytest
from nlp.nltk.nltk_tokenizer_task import NLTKTokenizerTask

tokenizerTask = NLTKTokenizerTask()


@pytest.mark.skip(reason="Por ahora no se testea NLTK")
def test_tokenizer1():
    executeTest("Hola", ["Hola"])


@pytest.mark.skip(reason="Por ahora no se testea NLTK")
def test_tokenizer2():
    executeTest("Hola. Tengo frío", ["Hola", "Tengo frío"])


# def test_tokenizer3():
#     executeTest(
#         "Yo me encuentro bien, tomo al despertar tiroxina para el tiroides, luego con el desayuno Valsartan luego Natecal, pastillas de calcio y en las comidas Alopurinol.",
#         [
#             "Yo me encuentro bien",
#             "tomo al despertar tiroxina para el tiroides, luego con el desayuno Valsartan luego Natecal, pastillas de calcio y en las comidas Alopurinol",
#         ],
#     )


def executeTest(text, expectedPhrases):
    phrases = tokenizerTask.execute(text)
    assert phrases == expectedPhrases
