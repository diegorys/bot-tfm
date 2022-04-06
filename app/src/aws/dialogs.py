import os
import json
from domain.knowledge import Knowledge
# from infrastructure.sqlite3.sqlite3_knowledge_repository import SQLite3KnowledgeRepository
# from infrastructure.dynamodb.dynamodb_knowledge_repository import DynamoDBKnowledgeRepository


def handle(event, context):
    # knowledgeRepository = SQLite3KnowledgeRepository("bot-tfm")
    # knowledges = knowledgeRepository.list()
    knowledges = [Knowledge(1, "pepe", "Hola", "basic", "saludar", "", "Hola pepe")]
    print('go')
    response = {"statusCode": 200, "knowledges": []}
    return response
