from flask import Blueprint, render_template

view_blueprint = Blueprint("view", __name__)

@view_blueprint.route("/")
def home():
    return render_template("index.html")

@view_blueprint.route("/home")
def home1():
    return render_template("index.html")