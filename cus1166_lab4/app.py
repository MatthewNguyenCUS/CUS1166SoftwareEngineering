#9/18/19 flask cont.
#blocks in html(research)
from flask import Flask, render_template

class_roster=[("John","A","Freshman"),
        ("Tom","B","Sophomore"),
        ("Mary","C","Freshman"),
        ("Lucas","B-","Junior"),
        ("Joan","D","Senior"),
        ("Jason","A+","Sophomore"),
        ("Anthony","A-","Junior")]

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/welcome/<string:student>")
def welcome(student):
    return render_template("welcome.html", student=student)


@app.route("/roster/<int:grade_view>")
def roster(grade_view):
    return render_template("roster.html", grade_view=grade_view, class_roster=class_roster)
