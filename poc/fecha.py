from datetime import datetime

# fecha = "2022-06-04T17:01:11+02:00"
fecha = "2022-06-04T17:01:11+02:00"
date = datetime.strptime(fecha, "%Y-%m-%dT%H:%M:%S+02:00")

print(date.strftime("%H:%M"))
