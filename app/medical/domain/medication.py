class Medication:
    def fromCommand(command):
        arguments = command.replace("recordar-medicamento", "").strip()
        list = arguments.split(" ")
        name = ""
        hour = ""
        day = ""
        frecuency = ""
        for item in list:
            keyValue = item.split("=")
            key = keyValue[0]
            value = keyValue[1].replace("'", "")
            if key == "medicamento":
                name = value
            elif key == "hora":
                hour = value
            elif key == "dia":
                day = value
            elif key == "frecuencia":
                frecuency = value
        return Medication(name, hour, day, frecuency)

    def __init__(self, name, hour, day, frecuency):
        self.name = name
        self.hour = hour
        self.day = day
        self.frecuency = frecuency
