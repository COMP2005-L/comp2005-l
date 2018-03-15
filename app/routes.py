from flask import render_template, flash, redirect, jsonify
from app import app
from app.controllers.login import Login
from app.controllers.post import PostController


@app.route("/login", methods=["GET"])
def login():
    return Login.get()


@app.route("/login", methods=["POST"])
def redirect():
    return Login.post()


@app.route("/postEdit", methods=["GET"])
@app.route("/postEdit/<int:postId>", methods=["GET"])
def show_post_editor(postId=None):
    return PostController.showPostEditor(postId)


@app.route("/postEdit", methods=["POST"])
@app.route("/postEdit/<int:postId>", methods=["POST"])
def create_update_post(postId=None):
    return PostController.post(postId)

@app.route("/Post", methods=["GET"])
def Post():
    return Post.post()
