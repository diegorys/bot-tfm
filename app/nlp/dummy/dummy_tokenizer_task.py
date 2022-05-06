from nlp.tasks.tokenizer_task import TokenizerTask


class DummyTokenizerTask(TokenizerTask):
    def execute(self, text: str):
        return [x.strip() for x in text.split(".")]
