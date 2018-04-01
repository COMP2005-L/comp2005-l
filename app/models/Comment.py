from app import db


class Comment(db.Model):
    """
        Represents a comment tied to a given post

        Attributes:
            id: int - The primary key ID identifying the comment
            body: string - The body text of the comment
            poster_id: int - The ID of the user who posted the comment
            post_id: int - The ID of the post the comment is attached to

        Examples:
            -To instantiate, use keyword parameters
            	example = Comment(body="This post is awesome!", poster_id=1, post_id=5)
    """
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(255), nullable=False)

    poster_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    postedby = db.relationship('User', uselist=False, lazy=False)

    post_id = db.Column(db.Integer, db.ForeignKey("post.id"), nullable=False)
    postedFor = db.relationship('Post', uselist=False, lazy=False)
