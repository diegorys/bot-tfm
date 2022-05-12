import os
import json
from dialogflow.templates.intent_template import IntentTemplate
from dialogflow.templates.user_says_template import UserSaysTemplate
from dialogflow.templates.entity_template import EntityTemplate
from dialogflow.templates.agent_template import AgentTemplate
from expert_system.domain import slots
from expert_system.domain import intents


class GenerateService:
    def __init__(self):
        self.agentTemplate = AgentTemplate()
        self.entityTemplate = EntityTemplate()
        self.userSaysTemplate = UserSaysTemplate()
        self.intentTemplate = IntentTemplate()

    def execute(self, data, path: str):
        print("Generate")
        if not os.path.exists(path):
            os.mkdir(path)
        entities = self.generateEntities(data)
        self.writeEntities(entities, path)
        intents = self.generateIntents(data)
        self.writeIntents(intents, path)
        self.generateAgent(path)
        self.generatePackage(path)

    def generateEntities(self, data):
        print("Generate entities")
        finalEntities = {}
        for item in data:
            entities = item["entities"]
            for entityName in entities.keys():
                print(f"{entityName}: {entities[entityName]}")
                if entityName not in finalEntities.keys():
                    finalEntities[entityName] = []
                if entities[entityName] not in finalEntities[entityName]:
                    finalEntities[entityName].append(entities[entityName])
        return finalEntities

    def writeEntities(self, entities, path):
        dir = f"{path}/entities"
        if not os.path.exists(dir):
            os.mkdir(dir)
        for entityName in entities.keys():
            output = self.entityTemplate.generate(entityName)
            os.makedirs(os.path.dirname(f"{dir}/{entityName}.json"), exist_ok=True)
            with open(f"{dir}/{entityName}.json", "w", encoding="utf-8") as f:
                json.dump(output, f, ensure_ascii=False, indent=4)
            output = self.generateValueTemplate(entityName, entities[entityName])
            os.makedirs(os.path.dirname(f"{dir}/{entityName}_entries_es.json"), exist_ok=True)
            with open(f"{dir}/{entityName}_entries_es.json", "w", encoding="utf-8") as f:
                json.dump(output, f, ensure_ascii=False, indent=4)
            output = self.generateValueTemplate(entityName, entities[entityName])

    def generateValueTemplate(self, entityName: str, values):
        output = []
        cKnowledge = ""
        if entityName in slots.keys():
            knowledge = slots[entityName]
            cKnowledge = json.dumps(knowledge)
            for key in knowledge.keys():
                output.append({"value": key, "synonyms": knowledge[key]})
        for value in values:
            if value not in cKnowledge:
                output.append({"value": value.lower(), "synonyms": []})
        return output

    def generateIntents(self, data):
        print("Generate intents")
        finalIntents = {}
        for item in data:
            intent = item["intent"]
            if "" != intent:
                if intent not in finalIntents.keys():
                    finalIntents[intent] = []
                finalIntents[intent].append({"text": item["text"], "entities": item["entities"]})
                # print(intent)
        return finalIntents

    def writeIntents(self, intents, path: str):
        dir = f"{path}/intents"
        print(dir)
        if not os.path.exists(dir):
            os.mkdir(dir)
        for intent in intents.keys():
            output = self.intentTemplate.generate(intent)
            with open(f"{path}/intents/{intent}.json", "w", encoding="utf-8") as f:
                json.dump(output, f, ensure_ascii=False, indent=4)
            output = self.generateTextsTemplate(intents[intent])
            with open(f"{path}/intents/{intent}_usersays_es.json", "w", encoding="utf-8") as f:
                json.dump(output, f, ensure_ascii=False, indent=4)

    def generateTextsTemplate(self, items):
        output = []
        for item in items:
            text = self.userSaysTemplate.generate(item["text"], item["entities"])
            output.append(text)
        return output

    def generateAgent(self, path: str):
        print("Generate agent")
        output = self.agentTemplate.generate("CuidadorMayores")
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
