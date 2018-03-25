from flask import render_template, session, redirect, url_for, request
from app.models.DiscussionGroup import DiscussionGroup
from app.models.User import User
from app import db

class memberList:

    """
    Handing viewing of member list when joined in a group
    """

    @staticmethod
    def members(userId):

        if session.get("logged_in"):

            if (userId):
                selectedUser = User.query.filter_by(username=request.form['username']).first()
                db.session.commit()
            return render_template("memberListView.html", id=selectedUser)

        else:
            return redirect("/GroupView")

