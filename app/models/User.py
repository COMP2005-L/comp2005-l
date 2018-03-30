from app import db
from app.models.DiscussionGroup import discussion_user

from datetime import datetime


class User(db.Model):
    """
        The model mapping to the User table

        Attributes:
            id: int - The primary key ID of the user
            username: string - The unique username used upon registration
            email: string - The unique email address used upon registration
            password: string - The user password used to login
            createdAt: datetime - The datetime at which the user instance was created

        Examples:
            -To instantiate, use keyword parameters
                example = User(username='e', email='me@me.com', password = 'test')
    """
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    createdAt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    groups = db.relationship("DiscussionGroup", secondary=discussion_user, back_populates="groupMemberships")
