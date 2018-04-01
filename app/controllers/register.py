from flask import render_template, flash, redirect, url_for, request, session
from app.models.User import User
from app import db

"""
Controller for registration

"""


class RegisterController:

    @staticmethod
    def get():
        """
        Handles returning the view for register page
            :return: jinjaTemplate

        """

        return render_template("registration.html")

    @staticmethod
    def post():

        """
            Handles returning the view for register page, and redirects user to post view once registeration is completed
            :return: jinjaTemplate

            """
        error = None
        if request.method == "POST":
            email = request.form.get("email")
            username = request.form.get("username")
            password1 = request.form.get("password1")
            password2 = request.form.get("password2")

            existentUsername = User.query.filter_by(username=username).first()
            existentEmail = User.query.filter_by(email=email).first()

            if (password1 != password2):
                error = "Passwords did not match!"
            elif (existentUsername or existentEmail):
                error = "Username or email already in use!"
            else:
                user = User(email=email, username=username, password=password1)
                db.session.add(user)
                db.session.commit()
                session["logged_in"] = user.id
                flash("You have successfully logged in!")
                return redirect(url_for('show_post_editor'))

        return render_template("registration.html", error=error)
