from flask import render_template, flash, redirect, jsonify
from app import app
from app.controllers.login import Login
from app.controllers.logout import Logout
from app.controllers.post import PostController
from app.controllers.group import GroupController
from app.controllers.register import RegisterController
from app.controllers.userprofile import UserProfile

@app.route("/")
@app.route("/login", methods=["GET"])
def login():
    return Login.get()



@app.route("/login", methods=["POST"])
def redirect():
    return Login.post()


@app.route("/logout", methods=["GET"])
def logout():
    return Logout.post()


@app.route("/register", methods=["GET"])
def showRegister():
    return RegisterController.get()


@app.route("/register", methods=["POST"])
def register():
    return RegisterController.post()


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


@app.route("/comments/create/<int:postId>", methods=["POST"])
def createComment(postId):
    return PostController.addComment(postId)


@app.route("/subscriptions/add/<int:postId>", methods=["POST"])
def subscribe(postId):
    return PostController.subscribe(postId)


@app.route("/subscriptions/remove/<int:postId>", methods=["POST"])
def unsubscribe(postId):
    return PostController.unsubscribe(postId)


@app.route("/userProfile/<string:username>", methods=["GET"])
def showUserProfile(username):
    return UserProfile.showUserProfile(username)

@app.route("/userProfile", methods=["POST"])
def create_direct_messaging_userprofile(userId):
    return UserProfile.directMessaging(userId)
