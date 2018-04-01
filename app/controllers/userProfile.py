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
            user = User.query.filter_by(username=username).first()
            post = Post.query.filter_by(id=postId).first()
            message = DirectMessaging.query.filter_by(id=messageId).first()

            if ( messageId != -1 ):
                notification = Notification(title='Unread message',
                                            body='You have new message!',
                                            read=False,
                                            ref='/user/{}'.format(user.id),
                                            recipient=user.id)

                db.session.add(notification)
                NotificationService.dispatch(notification)

            db.session.commit()


            return render_template("user_Profile.html", user=user, post=post)




    @staticmethod
    ## REQUIRES THE SOCKET ASPECT WHICH SAJID AND MOUSTAFA WILL WORK ON

    def directMessaging():
        """
            Handles returning the user to their profile page where they
            can view posts and direct message
        """



        return redirect("/userProfile")


