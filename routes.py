from os import getenv
from flask import redirect, render_template, request, session
from app import app

app.secret_key = getenv("SECRET_KEY")


@app.route("/")
def index():
    return render_template("index.html")