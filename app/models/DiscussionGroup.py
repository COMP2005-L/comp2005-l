from app import db

from datetime import datetime


class DiscussionGroup(db.Model):

    """
        The model mapping to the Discussion Group table

        Attributes:
            discussionid: int - The primary key ID of the Author
            discussiontitle: string - The unique title of what the new post is about
            discussionbody: string - The main information/data of the post.
            postedby: string - The name of the original author of the post.

        Examples:
            -To instantiate, use keyword parameters
                example = Post(title='e', body = 'i am a cat', poster_id = 1)
    """
    discussionid = db.Column(db.Integer, primary_key=True)
    discussiontitle = db.Column(db.String(50), unique=False, nullable=False)
    discussionbody = db.Column(db.String(255), nullable=False)
    discussiondateposted = db.Column(db.String(100), nullable=False)
    discussionposter_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    postedby = db.relationship('User', uselist=False, lazy=False)

