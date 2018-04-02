from flask import render_template, flash, redirect, url_for, request, session
from app.models.User import User

class Login:

    @staticmethod
    def get():
        """
        Handles returning the view for login page
        :return: jinjaTemplate
        """
        if session.get("logged_in"):
            return render_template("/ListView.html")
        else:
            return render_template("/login.html")

    @staticmethod
    def post():
        """
        Handles returning the view for logging in, and redirecting to post editor if successful
        :return: jinjaTemplate
        """
        error = None
        if request.method == "POST":
            user = User.query.filter_by(username=request.form['username']).first()
            if (not user):
                error = "Invalid Username!"
            elif user.password != request.form['password']:
                error = "Invalid Password!"
            else:
                session["logged_in"] = user.id
                flash("You have successfully logged in!")
                return redirect(url_for('list'))

        return render_template("login.html", error=error)

