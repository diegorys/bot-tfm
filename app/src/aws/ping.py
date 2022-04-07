try:
  import unzip_requirements
except ImportError:
  pass

import sys

def handle(event, context):
    return "pong"