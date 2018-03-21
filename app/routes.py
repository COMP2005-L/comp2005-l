from flask import render_template, flash, redirect, jsonify
from app import app
from app.controllers.login import Login
from app.controllers.post import PostController
from app.controllers.group import GroupController


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


@app.route("/post/<int:postId>", methods=["GET"])
def show_post(postId):
    return PostController.showPost(postId)


@app.route("/listview", methods=["GET"])
def list():
    return PostController.listPosts()


@app.route("/groups/create", methods=["POST"])
def createGroup():
    return GroupController.createGroup()


@app.route("/groups/create", methods=["GET"])
def showCreateGroup():
    return GroupController.showCreateGroup()
