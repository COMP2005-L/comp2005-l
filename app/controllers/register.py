from flask import render_template, flash, redirect, url_for, request
from app import app

class Register:

	@staticmethod
	def get():
		return render_template("registration.html")
	@staticmethod
	def post():
		error = None
		if request.method == "POST":
			if request.form[" email " ] != app.config[ "EMAIL" ]:
				error = "Invalid Email!"
			elif request.form [ "username" ] != app.config [ "USERNAME" ]:
                error = "Invalid Username!"
	        elif request.form [ "password" ] != app.config [ "PASSWORD" ]:
                error = "Invalid Password!"
			else:
				session[ "Register" ] = True
				flash("You have successfully Registered!")
				return redirect(url_for("Postview"))
                return render_template("registration.html", error=error)

