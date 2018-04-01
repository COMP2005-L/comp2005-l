from app import db

from datetime import datetime


class Post(db.Model):
    """
        The model mapping to the Post table

        Attributes:
            id: int - The primary key ID of the post
            title: string - The unique title of what the new post is about
            body: string - The main information/data of the post.
            poster_id: int - The id of the original author of the post.

        Examples:
            -To instantiate, use keyword parameters
                example = Post(title='e', body = 'i am a cat', poster_id = 1)
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=False, nullable=False)
    body = db.Column(db.String(255), nullable=False)
    poster_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    postedby = db.relationship('User', uselist=False, lazy=False)  # 1-1,auto-retrieved
