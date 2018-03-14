from flask import render_template, flash, redirect
from app import app
from app.controllers.login import Login
from app.controllers.register import Register


@app.route("/login", methods=["GET"])
def login():
	return Login.get()

@app.route("/login", methods=["POST"])
def redirect():
	return Login.post()

@app.route("/register", methods=["GET"])
def register():
    return Registration.get()

@app.route("/register", methods=["POST"])
def redirect():
        return Registration.post()



