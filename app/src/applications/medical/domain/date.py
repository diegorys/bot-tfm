from datetime import datetime


class Date:
    def __init__(self, date: str):
        self.date = date
        self.timestamp = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S+02:00").timestamp()
