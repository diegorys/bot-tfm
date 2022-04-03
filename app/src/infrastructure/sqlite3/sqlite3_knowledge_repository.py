import sqlite3
from domain.knowledge import Knowledge
from domain.knowledge_repository import KnowledgeRepository


class SQLite3KnowledgeRepository(KnowledgeRepository):
    def __init__(self, name):
        self.name = name
        con = sqlite3.connect("/database/" + name + ".db")
        cur = con.cursor()
        cur.execute(
            """CREATE TABLE IF NOT EXISTS knowledge
               (id INTEGER PRIMARY KEY AUTOINCREMENT, input TEXT, domain TEXT, intent TEXT, entities TEXT, response TEXT)"""
        )
        con.commit()
        con.close()

    def save(self, knowledge):
        query = f"INSERT INTO knowledge VALUES ('{knowledge.text}','{knowledge.domain}','{knowledge.intent}','{knowledge.entities}', '{knowledge.response}')"
        con = sqlite3.connect("/database/" + self.name + ".db")
        cur = con.cursor()
        cur.execute(query)
        con.commit()
        con.close()

    def list(self):
        con = sqlite3.connect("/database/" + self.name + ".db")
        cur = con.cursor()
        cur.execute("SELECT * FROM knowledge")
        rows = cur.fetchall()
        knowledges = []
        for row in rows:
            data = list(row)
            knowledge = Knowledge(data[0], data[1], data[2], data[3], data[4])
            knowledges.append(knowledge)
        con.close()
        return knowledges

    def listDomain(self, domain):
        con = sqlite3.connect("/database/" + self.name + ".db")
        cur = con.cursor()
        cur.execute(f"SELECT * FROM knowledge WHERE domain = '{domain}'")
        rows = cur.fetchall()
        knowledges = []
        for row in rows:
            data = list(row)
            knowledge = Knowledge(data[0], data[1], data[2], data[3], data[4])
            knowledges.append(knowledge)
        con.close()
        return knowledges

    def listIntent(self, intent):
        con = sqlite3.connect("/database/" + self.name + ".db")
        cur = con.cursor()
        cur.execute(f"SELECT * FROM knowledge WHERE intent = '{intent}'")
        rows = cur.fetchall()
        knowledges = []
        for row in rows:
            data = list(row)
            knowledge = Knowledge(data[0], data[1], data[2], data[3], data[4])
            knowledges.append(knowledge)
        con.close()
        return knowledges

    def truncate(self):
        con = sqlite3.connect("/database/" + self.name + ".db")
        cur = con.cursor()
        cur.execute("DELETE FROM knowledge")
        con.close()
