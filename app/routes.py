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


@app.route("/postview", methods=["GET"])
def postview():
    return None


@app.route("/postEdit/<int:postId>", methods=["POST"], defaults={'postId': None})
def create_update_post(postId):
	result = None
	try:
		result = PostController.post(postId)
	except:
		return jsonify({success: False})

	return jsonify(result)
