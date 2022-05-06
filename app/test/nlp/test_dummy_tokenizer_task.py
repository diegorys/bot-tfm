from nlp.dummy.dummy_tokenizer_task import DummyTokenizerTask

tokenizerTask = DummyTokenizerTask()


def test_tokenizer1():
    executeTest("Hola", ["Hola"])


def test_tokenizer2():
    executeTest("Hola. Tengo frío", ["Hola", "Tengo frío"])


def executeTest(text, expectedPhrases):
    phrases = tokenizerTask.execute(text)
    assert phrases == expectedPhrases
