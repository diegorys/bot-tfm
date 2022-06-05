from datetime import datetime, timedelta

# fecha = "2022-06-04T17:01:11+02:00"
fecha = "2022-06-04T17:01:11+02:00"
date = datetime.strptime(fecha, "%Y-%m-%dT%H:%M:%S+02:00")

print(date.strftime("%H:%M"))

timestamp = date.timestamp()
print(timestamp)

now = datetime.now().timestamp()
print(now)

minutes = (datetime.now() + timedelta(minutes=30)).timestamp()
print(minutes)