from app import db

from datetime import datetime



class DirectMessaging(db.Model):
    """
        The model mapping to the User Direct Messaging table

        Attributes:
            id: int - The primary key ID of the User sending a message.
            body: string - The body of the Users' direct message; Body of a post for example
            sender: string - The id of user sending the message
            recipient: integer - User id of the recipient of the direct message.
            date: datetime - The datetime at which the user created/sent the message.

        Examples:
            -To instantiate, use keyword parameters
            	example = DirectMessaging(body='text here', sender = 1, recipient=20)
    """
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(255), nullable=False)
    sender = db.relationship(db.String(50),db.ForeignKey("user.id"),nullable=False)
    recipient = db.Column(db.String(50), db.ForeignKey("user.id"), nullable=False)
    date = db.Column(db.Datetime, nullable=False)