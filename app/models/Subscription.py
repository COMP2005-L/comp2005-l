from app import db


class Subscription(db.Model):
    """
        The model mapping to the Subscription table

        Attributes:
            post: integer - Post ID user is subscribed to
            subscriber: integer - User ID of the subscriber

        Examples:
            -To instantiate, use keyword parameters
            	example = Subscription(post=20, subscriber=2)
    """
    post = db.Column(db.Integer, db.ForeignKey("post.id"), nullable=False)
    subscriber = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
