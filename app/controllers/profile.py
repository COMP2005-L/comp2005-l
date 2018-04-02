from flask import render_template, session, redirect, url_for, request
from app.models.User import User
class ProfileController:

    @staticmethod
    def showProfile():
        """
        Handles returning the view for user profiles
        :return:
        """
        user = User.query.filter_by(id=session["logged_in"]).first()
        return render_template('user_Profile.html', user=user)
