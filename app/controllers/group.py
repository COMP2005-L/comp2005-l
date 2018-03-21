from flask import render_template, session, redirect, request
from app.models.User import User
from app.services.JsonService import JsonService
from app import db
import json
from app.models.DiscussionGroup import DiscussionGroup
from app import db


class GroupController:

    @staticmethod
    def createGroup():
        """
        Handles creating new groups

        :return: redirect
        """

        groupName = request.form['groupName']
        groupMembers = request.form.getlist('groupMembers')

        newGroup = DiscussionGroup(groupName=groupName, groupMembers=groupMembers)
        db.session.add(newGroup)
        db.session.commit()

        return redirect('/listView')

    @staticmethod
    def showCreateGroup():
        """
        Handles returning the view for creating a group, providing the list of users of the application to the template
        :return: jinjaTemplate
        """

        users = User.query.order_by(User.username).all()
        dictUsers = [JsonService.prepareModel(user) for user in users]
        jsonUsers = json.dumps(dictUsers)
        return render_template("create_group.html", users=jsonUsers)
