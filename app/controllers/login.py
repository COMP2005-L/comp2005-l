from flask import render_template, flash, redirect, url_for, request
from app import app

class Login:

	@staticmethod
	def get():
		return render_template("login.html")
	@staticmethod	
	def post():
		error = None
		if request.method == "POST":
			if request.form[" username " ] != app.config[ "USERNAME" ]:
				error = "Invalid Username!"
			elif request.form [ "password" ] != app.config [ "PASSWORD" ]:
				error = "Invalid Password!"
			else:
				session[ "Login" ] = True
				flash("You have successfully logged in!")
				return redirect(url_for("Postview"))
			return render_template("login.html", error=error)
	
