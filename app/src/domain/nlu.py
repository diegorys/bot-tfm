class NLU:

  def getResponse(self, text):
    return text

  def identifyDomain(self, text):
    # SALUDAR, IDENTIFICAR USUARIO, MEDICINAS, BITÁCORA, NO ENTENDER...
    return 'NO_ENTENDER'

  def getIntent(self, domain, text):
    return ""
  
  def extractEntities(self, domain, intent, text):
    return {}