from flask import render_template, flash, redirect, url_for, request, session
from app.models.User import User


class Logout:
    @staticmethod
    def post():
        """
        Handles returning the view for logging out, and redirecting to login page
        :return: jinjaTemplate
        """
        logout_user()
        flash("You have successfully logged out!")
        return redirect(url_for('login'))
