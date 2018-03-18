from flask import render_template, flash, redirect
from app import app
from app.controllers.login import Login
from app.controllers.post import PostController


@app.route("/login", methods=["GET"])
def login():
    return Login.get()


@app.route("/login", methods=["POST"])
def redirect():
    return Login.post()


@app.route("/postview", methods=["GET"])
def postview():
    return None


@app.route("/listview", methods=["GET"])
def list():
    return Post.listPosts()
