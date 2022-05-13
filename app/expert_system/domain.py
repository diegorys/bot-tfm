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
        "soniase supra d": [],
        "atorvastatina": [],
        "lovastatina": [],
        "algidol": [],
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
