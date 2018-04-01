from app.tests.base.BaseFixture import BaseFixture
from app.controllers.group import GroupController
from app.models.User import User
from app.models.DiscussionGroup import DiscussionGroup
from app.models.Notification import Notification
from app.models.Subscription import Subscription

import unittest


class TestDiscussionGroups(BaseFixture):

    def setUp(self):
        super().setUp()
        user = User(username='user1', email='me@me.com', password='test')
        self.db.session.add(user)
        self.db.session.commit()
        self.userId = user.id

    def test_showCreateGroup(self):
        response = self.app.get("/groups/create")
        self.assertEqual(response.status_code, 200)  # route responds without errors
        self.assertTrue(b'</form>' in response.data)  # There is a form on the page

    def test_createGroup(self):
        self.app.post("/groups/create", data={
            "groupName": "myGroup",
            "groupMembers": [self.userId]
        })

        group = DiscussionGroup.query.filter_by(discussiontitle="myGroup").first()
        self.assertTrue(group)  # group exists
        self.assertEqual(len(group.groupMemberships), 1)  # group has one member



if __name__ == '__main__':
    unittest.main()
