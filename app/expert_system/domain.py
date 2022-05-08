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

intents = {"REGISTRAR_ESTADO": [{"slot": "estado", "required": True}]}
