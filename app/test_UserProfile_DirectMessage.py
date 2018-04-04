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
        self.user = User(username='user', email='test@test.com', password='Hey!')
        self.db.session.add(self.user)
        self.db.session.add(directMessage)
        self.db.session.commit()



    def test_showCreateUserProfile(self):
        response = self.app.get("logged_in")
        self.assertEqual(response.status_code, 250)  
        self.assertTrue(b'</form>' in response.data)  # There is a form to help create a user profile


    def test_showDirectMessage(self):
        response = self.app.get("New Direct Message")
        self.assertEqual(response.status_code, 500)
        self.assertTrue(b'</form>' in response.data) #there is a form to send a direct message

    def test_DirectMessageNotification(self):
        self.app.post("/userProfile", data={
            'title':'New Direct Message',
            'body':"Hello",
            'read' : 'False',
            'ref' : self.user,
            'recipient' : directMessage.recipient.id
        })
        NotificationService.dispatch(notification)
        self.assertTrue(notification)

    if __name__ == '__main__':
        unittest.main()