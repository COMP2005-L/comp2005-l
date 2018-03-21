from flask import render_template, session, redirect, request
from app.models.Group import Group
from app import db


class GroupController:

    @staticmethod
    def createGroup():
        """
        Handles creating new groups

        :return: result: dict
        """

        groupName = request.form('groupName')
        groupMembers = request.form('groupMembers')

        newGroup = Group(groupName=groupName, groupMembers=groupMembers)
        db.session.add(newGroup)
        db.session.commit()

        return redirect('/listView')
