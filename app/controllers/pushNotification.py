from flask import render_template, session, redirect, url_for, request
from flask_socketio import SocketIO
from app.models.User import User
from app.models.Notification import Notification
from app import db

class push_notification:
    
    @staticmethod
    def create_user_notification(user, action, title, message, reference):
        """
        Create a User Notification
        :param user: User object to send the notification to
        :param action: Action being performed
        :param title: The message title
        :param message: The body of message
        """
        user = User.query.filter_by(id=request.form['id']).first()
        notification = Notification(recipient=user, read=action, title=title, body=message, ref=reference)

        db.session.add(notification)
        db.session.commit()

    @socketio.on('message')
    def handle_user_notification(user, read, title, messsage, reference):
        """
        Push user notification to user socket connection.
        :param user: User object to send the notification to
        :param action: Action being performed
        :param title: The message title
        :param message: The body of message
        :param reference: Link relevent to the notification; Link to a post for example
        :param notification: a created notification
        """
        title = request.form('title')
        message = request.form('body')
        read = request.form('read')
        reference = request.form('ref')


        user = User.query.filter_by(id=request.form['id']).first()

        if not read:
            socket.broadcast.to('user').emit('response', {'meta': message, 'title': title, 'reference': reference }, callback=ack)
        db.session.delete(notification)

