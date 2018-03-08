from flask import render_template, flash, redirect, url_for, request, session
from app.models.User import User
class Login:

	@staticmethod
	def get():
		return render_template("login.html")

	@staticmethod	
	def post():
		error = None
		if request.method == "POST":
			print(request.form['username'])
			print(User.query.all())
			user = User.query.filter_by(username=request.form['username']).first()
			if (not user):
				error = "Invalid Username!"
			elif user.password != request.form['password']:
				error = "Invalid Password!"
			else:
				session[ "Login" ] = True
				flash("You have successfully logged in!")
				return redirect(url_for('postview'))
			return render_template("login.html", error=error)
	
