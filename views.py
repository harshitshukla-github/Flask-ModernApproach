import json
from flask import Blueprint, render_template

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