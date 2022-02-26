# to run FLASK_APP=app.py FLASK_ENV=development flask run

from flask import Flask, render_template, request

from api import repos_with_most_stars
from exceptions import GitHubApiError

app = Flask(__name__)

available_languages = ["Python", "JavaScript", "Ruby", "Java"]

@app.route("/", methods=["POST", "GET"])
def index():
    if request.method == "GET":
        selected_languages = available_languages
    elif request.method == "POST":
        selected_languages = request.form.getlist("languages")

    results = repos_with_most_stars(selected_languages)

    return render_template(
        "index.html", 
        selected_languages=selected_languages, 
        available_languages=available_languages, 
        results=results)