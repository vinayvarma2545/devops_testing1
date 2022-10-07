from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, purush!</p>"

@app.route("/k")
def hello_world1():
    return "<p>Hello, t!</p>"