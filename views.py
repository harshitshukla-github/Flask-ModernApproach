import json
from flask import Blueprint, render_template,redirect, url_for

view_blueprint = Blueprint("view", __name__)

with open("data.json", "r") as file:
    data = json.load(file)

print(data)

@view_blueprint.route("/")
def home():
    return render_template("index.html", data=data)

@view_blueprint.route("/home")
def home1():
    return render_template("index.html", data=data)

@view_blueprint.route("/vacancy")
def vacancy():
    # Assuming you have a route for the form, let's say 'form'
    return redirect(url_for("form"))

# Assuming you have a route for the form, let's say 'form'
@view_blueprint.route("/form")
def form():
    return render_template("form.html")