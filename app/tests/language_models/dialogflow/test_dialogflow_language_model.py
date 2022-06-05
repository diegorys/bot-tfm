from src.language_models.dialogflow.dialogflow_language_model import DialogflowLanguageModel


def test_identifyIntent():
    dfLM = DialogflowLanguageModel()
    intent, entities = dfLM.identifyIntent("Hola")
    assert intent != ""
    assert len(intent) > 0
    assert type(entities) is dict


def test_generateRequireParametersText():
    dfLM = DialogflowLanguageModel()
    dfLM.lastResponse = "Prueba"
    expected = "Prueba"

    received = dfLM.generateRequireParametersText(None)

    assert expected == received


def test_generateText():
    dfLM = DialogflowLanguageModel()
    dfLM.lastResponse = "Prueba"
    expected = "Prueba"

    received = dfLM.generateText(None)

    assert expected == received


def test_parseDateTime_object():
    dfLM = DialogflowLanguageModel()
    dateTime = [{"date_time": "2022-08-25T04:00:00+02:00"}]
    cuando = dfLM.parseDateTime(dateTime)
    assert cuando == "2022-08-25T04:00:00+02:00"


def test_parseDateTime_single():
    dfLM = DialogflowLanguageModel()
    dateTime = ["2022-06-04T12:00:00+02:00"]
    cuando = dfLM.parseDateTime(dateTime)
    assert cuando == "2022-06-04T12:00:00+02:00"


def test_parseDateTime_startEndDateTime():
    dfLM = DialogflowLanguageModel()
    dateTime = [
        {"startDateTime": "2022-06-04T16:18:01+02:00", "endDateTime": "2022-06-04T16:48:01+02:00"}
    ]
    cuando = dfLM.parseDateTime(dateTime)
    assert cuando == "2022-06-04T16:48:01+02:00"


def test_parseDateTime_startEndTime():
    dfLM = DialogflowLanguageModel()
    dateTime = [{"startTime": "2022-06-05T05:00:00+02:00", "endTime": "2022-06-05T11:59:59+02:00"}]
    cuando = dfLM.parseDateTime(dateTime)
    assert cuando == "2022-06-05T11:59:59+02:00"


def test_parseDateTime_startEndDate():
    dfLM = DialogflowLanguageModel()
    dateTime = [{"startDate": "2022-06-06T00:00:00+02:00", "endDate": "2022-06-09T23:59:59+02:00"}]
    cuando = dfLM.parseDateTime(dateTime)
    assert cuando == "2022-06-09T23:59:59+02:00"
