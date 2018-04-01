from flask import render_template, session, redirect, url_for, request
from app.models.Post import Post
from app.models.User import User
from app.services.NotificationService import NotificationService
from app import db


class UserProfile:

    @staticmethod
    def showUserProfile(username):
        """
            Handles the get method for the user to their profile page where they
            can view posts and direct message
            :return: jinjaTemplate

        """
        
        if (session.get("logged_in")):
            user = User.query.filter_by(username = username).first()
            return render_template("user_Profile.html", user=user)


    @staticmethod
    ## REQUIRES THE SOCKET ASPECT WHICH SAJID AND MOUSTAFA WILL WORK ON

    def directMessaging():
        """
            Handles returning the user to their profile page where they
            can view posts and direct message


        """

        return redirect("/userProfile")