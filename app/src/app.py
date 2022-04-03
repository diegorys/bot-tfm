# save this as app.py
import json
from flask import Flask, render_template
from infrastructure.sqlite3.sqlite3_knowledge_repository import SQLite3KnowledgeRepository

app = Flask(__name__, template_folder='/templates')


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/knowledges")
def knowledges():
    knowledgeRepository = SQLite3KnowledgeRepository("bot-tfm")
    knowledges = knowledgeRepository.list()
    html = render_template("knowledges.html", knowledges=knowledges)
    return html


app.run(host="0.0.0.0")
