from .. import app
from flask import render_template

@app.route("/")
def index():
    return "<h1>HELLO, IT'S ME</h1>"

@app.route("/app1")
def app1():
    return {"mama": "mila", "saba": "sama", "amogus": "died"}

@app.route("/app2")
def app2():
    return "mama mila ramu"


@app.route("/app3")
def app3():
    context = {
        1: "Win",
        2: "Loss",
    }
    return render_template("for_loop.html", context=context)