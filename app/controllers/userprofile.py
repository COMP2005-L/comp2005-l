from flask import render_template, session, redirect, url_for, request
from app.models.Post import Post
from app.models.User import User
from app.services.NotificationService import NotificationService
from app import db


class UserProfile:

    @staticmethod
    def showUserProfile():
        return render_template("user_Profile.html")

    @staticmethod
    def directMessaging():
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
                return redirect(url_for('show_post_editor'))

        return render_template("login.html", error=error)
