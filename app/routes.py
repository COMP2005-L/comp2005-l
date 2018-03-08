from flask import render_template, flash, redirect
from app import app
from app.controllers.login import Login


@app.route("/login", methods=["GET"])
def login():
	return Login.get()

@app.route("/login", methods=["POST"])
def redirect():
	return Login.post()
