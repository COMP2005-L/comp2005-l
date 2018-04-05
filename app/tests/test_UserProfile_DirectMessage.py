import flask
from flask import request, session
from app.tests.base.BaseFixture import BaseFixture
from app.models.User import User
from app.models.DirectMessaging import DirectMessaging
from app.services.MessagingService import MessagingService
from app.services.NotificationService import NotificationService
from app.models.Notification import Notification
from app import app

import unittest


class TestUserProfileDirectMessage(BaseFixture):

    def setUp(self):
        super().setUp()
        user = User(username='user', email='test@test.com', password='Hey!')
        user2 = User(username='user2', email='test2@test.com', password='Hey!')
        self.db.session.add(user)
        self.db.session.add(user2)
        self.db.session.commit()
        self.userId = user.id
        self.username = user.username
        self.userEmail = user.email
        self.user2name = user2.username

    def test_showCreateUserProfile(self):
        with self.app as c:
            with c.session_transaction() as session:
                session["logged_in"] = self.userId
            response = self.app.get("/userProfile/{}".format(self.username))
            self.assertEqual(response.status_code, 200)
            self.assertTrue(self.username.encode() in response.data)  # The username is on the page
            self.assertTrue(self.userEmail.encode() in response.data)  # The user email is on the page

    def test_showDirectMessage(self):
        with self.app as c:
            with c.session_transaction() as session:
                session["logged_in"] = self.userId
            response = self.app.get("/userProfile/{}".format(self.user2name))
            self.assertEqual(response.status_code, 200)
            self.assertTrue(b'</form>' in response.data)  # there is a form to send a direct message

    def test_DirectMessageNotification(self):
        with self.app as c:
            with c.session_transaction() as session:
                session["logged_in"] = self.userId

            c.post("/userProfile/{}".format(self.userId), data={
                'body': "Hello",
            })
            notification = Notification.query.filter_by(title='New Direct Message').first()
            self.assertTrue(notification)  # A notification has been created for the direct messaging event

if __name__ == '__main__':
	unittest.main()
