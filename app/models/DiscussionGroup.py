from app import db
from app.models.User import User

from datetime import datetime

discussion_user = db.Table("discussion_user", db.Model.metadata, \
                             db.Column("discussion_id", db.Integer, db.ForeignKey("discussion.discussionid")), \
                             db.Column("user_id", db.Integer, db.ForeignKey("user.id")))



class DiscussionGroup(db.Model):

    """
        The model mapping to the Discussion Group table

        Attributes:
            discussionid: int - The primary key ID of the Author
            discussiontitle: string - The unique title of what the new post is about
            discussiondateposted: string - The date in which the discussion group was created
        Examples:
            -To instantiate, use keyword parameters
                example = DiscussionGroup(discussiontitle = "Awesome Group!",  discussiondateposted = <<today's date>>)
    """



    __tablename__ = "discussion"
    discussionid = db.Column(db.Integer, primary_key=True)
    discussiontitle = db.Column(db.String(50), unique=False, nullable=False)
    discussiondateposted = db.Column(db.DateTime, onupdate=db.datetime.now)


    groupMembership = db.relationship("User", secondary = discussion_user)

