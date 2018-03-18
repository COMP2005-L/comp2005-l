from flask import render_template, flash, redirect, url_for, request, session
from app.models.Post import Post
from app import db

class PostController:

    @staticmethod
    def showListView():
        return render_template("ListView.html")

    @staticmethod
    def listPosts():

        if session.get("logged_in"):
            posts = Post.query.all().order_by(Post.title)
            return render_template("ListView.html", posts=posts)

        else:
            return redirect("/login")