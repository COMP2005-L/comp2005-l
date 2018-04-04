from flask import session
from app import db
from app.models.Notification import Notification
from app.models.User import User
from app.models.DirectMessaging import DirectMessaging
from app.services.NotificationService import NotificationService


class MessagingService:

    @staticmethod
    def send(directMessage):
        """
        Sends a given direct message to the user, by persisting the direct message, and sending
        a notification to the recipient

        :param directMessage: DirectMessaging - The message to be sent
        :return: None
        """
        db.session.add(directMessage)
        db.session.commit()
        notification = Notification(title='New Direct Message',
                                    body='From {}'.format(directMessage.sender.username),
                                    read=False,
                                    ref='/userProfile/{}'.format(directMessage.sender.username),
                                    recipient=directMessage.recipient.id)

        db.session.add(notification)
        db.session.commit()
        NotificationService.dispatch(notification)

    @staticmethod
    def getConversation(targetUser):
        """
        Retrieves the conversation between the target user and the currently logged in user

        :param targetUser: User
        :return: list<DirectMessaging>
        """
        previewingUser = User.query.filter_by(id=session.get("logged_in")).first()
        query1 = DirectMessaging.query.filter(DirectMessaging.sender_id == targetUser.id,
                                              DirectMessaging.recipient_id == previewingUser.id).all()
        query2 = DirectMessaging.query.filter(DirectMessaging.sender_id == previewingUser.id,
                                              DirectMessaging.recipient_id == targetUser.id).all()
        query1.extend(query2)
        query1.sort(key=lambda message: message.date, reverse=True)

        return query1
