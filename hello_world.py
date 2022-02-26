from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello world!"

@app.route("/name/<name>")
def hello_name(name):
    return f"Hello {name}"