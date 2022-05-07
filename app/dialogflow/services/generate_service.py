import os
import json


class GenerateService:
    def execute(self, data, path: str):
        print("Generate")
        self.generateEntities(data, path)
        self.generateIntents(data, path)
        self.generateAgent(path)
        self.generatePackage(path)

    def generateEntities(self, data, path: str):
        print("Generate entities")
        dir = f"{path}/entities"
        if not os.path.exists(dir):
            os.mkdir(dir)
        finalEntities = {}
        for item in data:
            entities = item["entities"]
            for entityName in entities.keys():
                print(f"{entityName}: {entities[entityName]}")
                if entityName not in finalEntities.keys():
                    finalEntities[entityName] = []
                if entities[entityName] not in finalEntities[entityName]:
                    finalEntities[entityName].append(entities[entityName])
        self.writeEntities(finalEntities, dir)

    def writeEntities(self, entities, path):
        for entityName in entities.keys():
            output = self.generateEntityTemplate(entityName)
            os.makedirs(os.path.dirname(f"{path}/{entityName}.json"), exist_ok=True)
            with open(f"{path}/{entityName}.json", "w", encoding="utf-8") as f:
                json.dump(output, f, ensure_ascii=False, indent=4)
            output = self.generateValueTemplate(entities[entityName])
            os.makedirs(os.path.dirname(f"{path}/{entityName}_entries_es.json"), exist_ok=True)
            with open(f"{path}/{entityName}_entries_es.json", "w", encoding="utf-8") as f:
                json.dump(output, f, ensure_ascii=False, indent=4)
            output = self.generateValueTemplate(entities[entityName])

    def generateEntityTemplate(self, entityName):
        return {
            "id": "xxx",
            "name": entityName,
            "isOverridable": True,
            "isEnum": False,
            "isRegexp": False,
            "automatedExpansion": False,
            "allowFuzzyExtraction": False,
        }

    def generateValueTemplate(self, values):
        output = []
        for value in values:
            output.append({"value": value, "synonyms": []})
        return output

    def generateIntents(self, data, path: str):
        print("Generate intents")
        dir = f"{path}/intents"
        print(dir)
        if not os.path.exists(dir):
            os.mkdir(dir)
        for item in data:
            intent = item["intent"]
            if "" != intent:
                # print(intent)
                output = {"id": "", "name": intent}
                with open(f"{path}/intents/{intent}.json", "w", encoding="utf-8") as f:
                    json.dump(output, f, ensure_ascii=False, indent=4)
                with open(f"{path}/intents/{intent}_usersays_es.json", "w", encoding="utf-8") as f:
                    json.dump(output, f, ensure_ascii=False, indent=4)

    def generateAgent(self, path: str):
        print("Generate agent")
        output = {
            "description": "",
            "language": "es",
            "shortDescription": "",
            "examples": "",
            "linkToDocs": "",
            "displayName": "CuidadorMayores",
            "disableInteractionLogs": False,
            "disableStackdriverLogs": True,
            "defaultTimezone": "Europe/Madrid",
            "isPrivate": True,
            "mlMinConfidence": 0.3,
            "supportedLanguages": [],
            "enableOnePlatformApi": True,
            "onePlatformApiVersion": "v2",
            "secondaryKey": "51531c8d9a204b39b93fa09f4a8d21e3",
            "analyzeQueryTextSentiment": False,
            "enabledKnowledgeBaseNames": [],
            "knowledgeServiceConfidenceAdjustment": 0.0,
            "dialogBuilderMode": False,
            "baseActionPackagesUrl": "",
            "enableSpellCorrection": False,
        }
        print(f"{path}/agent.json")
        os.makedirs(os.path.dirname(f"{path}/agent.json"), exist_ok=True)
        with open(f"{path}/agent.json", "w", encoding="utf-8") as f:
            json.dump(output, f, ensure_ascii=False, indent=4)

    def generatePackage(self, path: str):
        print("Generate package")
        output = {"version": "1.0.0"}
        print(f"{path}/package.json")
        os.makedirs(os.path.dirname(f"{path}/package.json"), exist_ok=True)
        with open(f"{path}/package.json", "w", encoding="utf-8") as f:
            json.dump(output, f, ensure_ascii=False, indent=4)
