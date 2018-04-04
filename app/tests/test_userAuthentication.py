import flask
from flask import request, session
from app.tests.base.BaseFixture import BaseFixture
from app.controllers.login import Login
from app.models.User import User
from app import app

import unittest


class TestUserAuthentication(BaseFixture):

    def setUp(self):

        super().setUp()
        self.user = User(username='user', email='test@test.com', password='Hello')
        self.db.session.add(self.user)
        self.db.session.commit()

    def test_showLogin(self):

        response = self.app.get("/login")
        self.assertTrue(b'</form>' in response.data) # This shows if the username and password form is displayed

    def test_Login(self):
        response = self.app.post("/login", data={"username": "user", "password": "Hello"}, follow_redirects=True)
        self.assertTrue(b'navbar' in response.data)  # logged in users see the navbar

    def test_Registration(self):

        self.app.post("/register", data = {"username": "user2","email":"test2@test.com", "password1": "1234", "password2": "1234"})
        newUser = User.query.filter_by(username = "user2").first()
        allUsers = User.query.all()

        self.assertTrue(newUser) # Checks to see if user is registered
        self.assertEqual(len(allUsers),2) # Number of users is 2

if __name__ == '__main__':
    unittest.main()