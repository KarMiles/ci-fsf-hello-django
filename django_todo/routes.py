from flask import render_template
from django_todo import app, db


@app.route("/")
def home():
    return render_template("add_item.html")
