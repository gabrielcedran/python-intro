from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello world!"

@app.route("/name/<name>")
def hello_name(name):
    return f"Hello {name}"

@app.route("/sample-with-template")
def test_template():
    return render_template("sample.html")