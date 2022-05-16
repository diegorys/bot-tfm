slots = {
    "estado": {
        "tristeza": ["triste", "tristeza", "disgustado", "disgustada", "mal"],
        "alegría": ["alegría", "alegre", "contento", "feliz", "felicidad", "bien"],
        "soledad": ["solo", "sola", "soledad", "solitaria", "solitario"],
        "cansancio": ["cansancio", "agotamiento", "cansado", "cansada", "agotado", "agotada"],
    },
    "medicamento": {
        "ibuprofeno": [],
        "rinialer": [],
        "metformina": [],
        "paracetamol": [],
        "soniase supra d": ["soniase supra d", "soniase"],
        "atorvastatina": [],
        "lovastatina": [],
        "algidol": [],
        "rosa mosqueta": []
    },
    "cita": {
        "dentista": ["dentista", "odontólogo", "odontóloga", "odontología"],
        "dermatólogo": ["dermatólogo, dermatóloga", "dermatología"],
        "alergólogo": [],
        "cardiólogo": [],
        "médico de cabecera": [],
        "enfermero": [],
    },
}

intents = {
    # BÁSICO
    "REGISTRAR_SALUDO": [],
    "REGISTRAR_DESPEDIDA": [],
    # ESTADO DE ÁNIMO
    "REGISTRAR_ESTADO_EMOCIONAL": [{"name": "estado", "required": True}],
    # MÉDICO
    "REGISTRAR_TOMA_MEDICAMENTO": [
        {"name": "medicamento", "required": True},
        {"name": "cuando", "required": True},
    ],
    "REGISTRAR_CITA_MEDICA": [
        {"name": "cita", "required": True},
        {"name": "cuando", "required": True},
    ],
    # OTROS
}

responses = {
    # BÁSICO
    "REGISTRAR_SALUDO": [
        "Hola, ¿qué tal estás?",
        "Hola, ¿quieres registrar algún medicamento?",
        "Hola, ¿quieres registrar alguna cita médica?",
        "Hola, ¿qué tal te encuentras?",
    ],
    "REGISTRAR_DESPEDIDA": [
        "Hablamos en otra ocasión",
        "Me alegro de que hayamos hablado",
        "No dudes en escribirme si necesitas algo más",
        "Hasta luego",
        "Hasta la próxima",
        "¡Nos vemos!",
        "Me ha gustado hablar contigo, ¡hasta luego!",
    ],
    # ESTADO DE ÁNIMO
    "REGISTRAR_ESTADO_EMOCIONAL": [
        "Registro tu estado de ánimo: [estado]",
        "Estado de ánimo anotado: [estado]",
        "Entiendo tu estado de [estado]",
    ],
    # MÉDICO
    "REGISTRAR_TOMA_MEDICAMENTO": [
        "Tienes que tomar [medicamento] [cuando]",
        "Anoto medicamento [medicamento] [cuando]",
        "Te recordaré que tomes [medicamento] [cuando]",
        "[cuando] tomar [medicamento]. Anotado queda.",
    ],
    "REGISTRAR_CITA_MEDICA": [
        "Tienes una cita médica: [cita] [cuando]",
        "Anoto cita médica: [cita] [cuando]",
        "Te recordaré la cita médica: [cita] [cuando]",
        "[cuando] cita médica [cita]. Anotado queda.",
    ],
}
