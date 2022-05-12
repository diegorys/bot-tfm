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
    },
}

intents = {
    "REGISTRAR_ESTADO_EMOCIONAL": [{"name": "estado", "required": True}],
    "REGISTRAR_TOMA_MEDICAMENTO": [
        {"name": "medicamento", "required": True},
        {"name": "cuando", "required": True},
    ],
    "REGISTRAR_SALUDO": [],
    "REGISTRAR_DESPEDIDA": [],
    "REGISTRAR_CITA_MEDICA": [
        {"name": "cita", "required": True},
        {"name": "cuando", "required": True},
    ],
}
