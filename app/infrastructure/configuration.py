import os

class Config:
  def __init__(self):
    self.TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
    self.SERVICE_STATUS = os.environ.get("SERVICE_STATUS") or 0
    self.SERVICE_AVAILABLE = int(self.SERVICE_STATUS) == 1
