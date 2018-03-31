from flask import render_template, session, redirect, url_for, request
from app.models.Post import Post
from app.models.User import User
from app.services.NotificationService import NotificationService
from app import db


class UserProfile:




    @staticmethod
    def showUserProfile(username, postId):
        """
            Handles the get method for the user to their profile page where they
            can view posts and direct message
            :return: jinjaTemplate

        """
        
        if (session.get("logged_in")):
            user = User.query.filter_by(username = username).first()
            post = Post.query.filter_by(id = postId).first()
            return render_template("user_Profile.html",user = user, post = post)


    @staticmethod
    def directMessaging(userId):
        """
            Handles returning the user to their profile page where they
            can view posts and direct message
            :param userId: User to send direct message to
            :return: jinjaTemplate

        """

        title = request.form["title"]
        body = request.form["body"]
        postedBy = request.form["postedBy"]


        postedBy = User.query.filter_by(id=session["logged_in"]).first()
        newPost = Post(title = title, body = body, postedBy = postedBy)
        db.session.add(newPost)
        db.session.commit()

        return redirect("/userProfile")