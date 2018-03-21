from app import db

from datetime import datetime


class Post(db.Model):
    """
        The model mapping to the Post table

        Attributes:
            id: int - The primary key ID of the Author
            title: string - The unique title of what the new post is about
            body: string - The main information/data of the post.
            postedby: string - The name of the original author of the post.

        Examples:
            -To instantiate, use keyword parameters
                example = Post(title='e', body = 'i am a cat', poster_id = 1)
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=False, nullable=False)
    body = db.Column(db.String(255), nullable=False)
    poster_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    postedby = db.relationship('User', uselist=False, lazy=False)  # 1-1, auto-retrieved

    def subscribe(self, post):
        if not self.is_subscribing(post):
            self.subcribed.append(post)

    def unsubscribe(self, post):
        if self.is_subscribing(post):
            self.subscribed.remove(post)

    def is_subscribing(self, post):
        return self.subscribed.filter(
            subscribers.c.subscribed_id == Post.id).count() > 0

    def subscribed_posts(self):
        return Post.query.join(
            subscribers, (subscribers.c.subscribed_id_id == Post.id)).filter(
            subscribers.c.subscribed_id == self.id).order_by(
            Post.title())
