import sqlite3
from app.src.domain.dialog import Dialog
from app.src.domain.dialog_repository import DialogRepository


class DynamoDBDialogRepository(DialogRepository):
    def __init__(self, name):
        self.name = name
        con = sqlite3.connect("/database/" + name + ".db")
        cur = con.cursor()
        cur.execute(
            """CREATE TABLE IF NOT EXISTS knowledge
               (userid INTEGER, username TEXT, input TEXT, domain TEXT, intent TEXT, entities TEXT, response TEXT)"""
        )
        con.commit()
        con.close()

    def save(self, user, knowledge):
        # query = f"INSERT INTO knowledge VALUES ('{knowledge.text}','{knowledge.domain}','{knowledge.intent}','{knowledge.entities}', '{knowledge.response}')"
        query = f"INSERT INTO knowledge VALUES ({user.id}, '{user.name}', '{knowledge.text}','{knowledge.domain}','{knowledge.intent}','{knowledge.entities}', '{knowledge.response}')"
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
            knowledge = Dialog(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
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
            knowledge = Dialog(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
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
            knowledge = Dialog(data[0], data[1], data[2], data[3], data[4], data[5], data[6])
            knowledges.append(knowledge)
        con.close()
        return knowledges

    def truncate(self):
        con = sqlite3.connect("/database/" + self.name + ".db")
        cur = con.cursor()
        cur.execute("DELETE FROM knowledge")
        con.close()
