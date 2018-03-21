from app import db


class Notification(db.Model):
    """
        The model mapping to the Notification table

        Attributes:
            title: string - Title of the notification; Title of a post for example
            body: string - The body of the notification; Body of a post for example
            read: boolean - True if notification has been seen, false if it hasn't
            ref: string - Link relevent to the notification; Link to a post for example
            recipient: integer - User ID of the recipient

        Examples:
            -To instantiate, use keyword parameters
            	example = Notification(title='title', body='text here', read=True, ref='link' recipient=20)
    """
    title = db.Column(db.String(40), nullable=False)
    body = db.Column(db.String(255), nullable=False)
    read = db.Column(db.Boolean, nullable=False)
    ref = db.Column(db.String(255), nullable=False)
    recipient = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
