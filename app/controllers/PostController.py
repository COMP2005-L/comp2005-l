from flask import render_template, flash, redirect, url_for, request, session
from app.models.Post import Post

class PostController:

	@staticmethod
	def showListView():
        return render_template("ListView.html")
