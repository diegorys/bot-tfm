import nltk
from nlp.tasks.tokenizer_task import TokenizerTask


class NLTKTokenizerTask(TokenizerTask):
    def __init(self):
        nltk.download("punkt")

    def execute(self, text: str):
        spanish_tokenizer = nltk.data.load("tokenizers/punkt/PY3/spanish.pickle")
        tokens = spanish_tokenizer.tokenize(text)
        print(f"Text: {text}")
        print(tokens)
        return tokens
