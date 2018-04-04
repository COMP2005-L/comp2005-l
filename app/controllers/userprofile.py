from flask import render_template, session, redirect, url_for, request
from app.models.Post import Post
from app.models.User import User
from app.models.DirectMessaging import DirectMessaging
from app.services.MessagingService import MessagingService
from app import db


class UserProfile:

    @staticmethod
    def showUserProfile():

        """
        Handles returning the view for user profiles
        :return:

        """

        user = User.query.filter_by(id=session.get("logged_in")).first()
        return render_template('user_Profile.html', user=user)

    @staticmethod
    def getUserMessages(username):
        """
            Handles the get method for the user to their profile page where they
            can view posts and direct message
            :return: jinjaTemplate

        """
        
        if (session.get("logged_in")):
            user = User.query.filter_by(username = username).first()
            messages = MessagingService.getConversation(user)

            return render_template("user_Profile.html", user=user, messages=messages)


    @staticmethod
    def directMessaging(recipientId):
        """
            Handles sending a direct message to the targeted user
            :return: redirect
        """
        body = request.form.get("body")
        sender_id = session["logged_in"]
        dm = DirectMessaging(body=body, sender_id=sender_id, recipient_id=recipientId)
        MessagingService.send(dm)

        return redirect("/userProfile/{}".format(dm.recipient.username))
