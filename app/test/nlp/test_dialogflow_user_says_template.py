from dialogflow.templates.user_says_template import UserSaysTemplate

userSaysTemplate = UserSaysTemplate()


def test_generate_hola():
    #     expected = {
    #         "data": [
    #             {
    #                 "text": "Hola",
    #                 "userDefined": False,
    #             }
    #         ],
    #         "isTemplate": False,
    #         "count": 0,
    #         "lang": "es",
    #         "updated": 0,
    #     }
    #     received = userSaysTemplate.generate("Hola", {})
    #     assert received == expected

    # def test_generate_estado():
    #     expected = {
    #         "data": [
    #             {
    #                 "text": "Hola, ",
    #                 "userDefined": False,
    #             },
    #             {
    #                 "text": "estoy",
    #                 "meta": "@estado",
    #                 "alias": "estado",
    #                 "userDefined": False,
    #             },
    #             {
    #                 "text": "bien",
    #                 "userDefined": False,
    #             },
    #         ],
    #         "isTemplate": False,
    #         "count": 0,
    #         "lang": "es",
    #         "updated": 0,
    #     }
    received = userSaysTemplate.generate(
        "Hola, estoy bien, estoy viendo una serie",
        {"estado": "bien", "actividad": "viendo una serie"},
    )
    assert True == False
    # assert received == expected
