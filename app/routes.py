from flask import render_template, flash, redirect
from app import app
from app.forms import LoginForm
from app.controllers.login import Login


@app.route("/login", methods=["GET"])
def login():
	login.get()

@app.route("/login", methods=["POST"])
def redirect():
	login.post()
