from dialogflow.templates.user_says_template import UserSaysTemplate

userSaysTemplate = UserSaysTemplate()


def test_generate_hola():
    expected = {
        "data": [
            {
                "text": "Hola",
                "userDefined": False,
            }
        ],
        "isTemplate": False,
        "count": 0,
        "lang": "es",
        "updated": 0,
    }
    received = userSaysTemplate.generate("Hola", {})
    assert received == expected


def test_generate_estado():
    expected = {
        "data": [
            {
                "text": "Hola, estoy ",
                "userDefined": False,
            },
            {
                "text": "bien",
                "meta": "@estado",
                "alias": "estado",
                "userDefined": False,
            },
            {
                "text": ", estoy viendo una serie",
                "userDefined": False,
            },
        ],
        "isTemplate": False,
        "count": 0,
        "lang": "es",
        "updated": 0,
    }
    received = userSaysTemplate.generate(
        "Hola, estoy bien, estoy viendo una serie",
        {"estado": "bien"},
    )
    print(received)
    assert received == expected


def test_generate_medicamento():
    expected = {
        "data": [
            {
                "text": "Todos los meses el día ocho",
                "meta": "@sys.date-time",
                "alias": "date-time",
                "userDefined": False,
            },
            {
                "text": " me toca la ",
                "userDefined": False,
            },
            {
                "text": "vitamina d",
                "meta": "@medicamento",
                "alias": "medicamento",
                "userDefined": False,
            },
        ],
        "isTemplate": False,
        "count": 0,
        "lang": "es",
        "updated": 0,
    }
    received = userSaysTemplate.generate(
        "Todos los meses el día ocho me toca la vitamina d",
        {"cuando": "Todos los meses el día ocho", "medicamento": "vitamina d"},
    )
    print(received)
    assert received == expected
