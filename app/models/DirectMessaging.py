from app import db

from datetime import datetime



class DirectMessaging(db.Model):
    """

        The model mapping to the User Direct Messaging table

        Attributes:
            id: int - The primary key ID identifying the direct message
            body: string - The body of the Users' direct message; Body of a post for example
            sender_id: int - The id of user sending the message
            recipient_id: integer - User id of the recipient of the direct message.
            date: datetime - The datetime at which the user created/sent the message.

        Examples:
            -To instantiate, use keyword parameters
            	example = DirectMessaging(body='text here', sender_id = 1, recipient_id=20)
    
    """
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(255), nullable=False)

    sender_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    sender = db.relationship('User', uselist=False, lazy=False, foreign_keys=[sender_id])  # single, auto-retrieved

    recipient_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    recipient = db.relationship('User', uselist=False, lazy=False,
                                foreign_keys=[recipient_id])  # single, auto-retrieved

    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
