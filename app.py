from flask import Flask

app = Flask(__name__)

@app.route("/")
def getHome():
    return "Home"

@app.route("/user")
def getUsers():
    return {"users": ["João", "Maria", "José"]}

@app.route("/user/<id>")
def getUser(id):
    return { "id": id, "nickname": "João", "email": "joao@email.com", "role": 0 }