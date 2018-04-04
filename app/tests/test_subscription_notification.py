from app.tests.base.BaseFixture import BaseFixture
from app.models.User import User
from app.models.Post import Post
from app.models.Comment import Comment
from app.models.Subscription import Subscription
from app.models.Notification import Notification
from app.services.SubscriptionService import SubscriptionService
from app.services.NotificationService import NotificationService

import unittest


class TestSubscriptionNotification(BaseFixture):

    def setUp(self):
        super().setUp()
        user1 = User(username='user1', email='test@test.com', password='test')
        user2 = User(username='user2', email='test2@test.com', password='test')
        self.db.session.add(user1)
        self.db.session.add(user2)
        self.db.session.commit()
        post = Post(title="title", body="body", poster_id=user1.id)
        self.db.session.add(post)
        self.db.session.commit()
        self.user1Id = user1.id
        self.user2Id = user2.id
        self.postId = post.id


    def test_subscription(self):
        SubscriptionService.subscribe(self.postId, self.user2Id)
        subscription = Subscription.query.filter_by(post=self.postId).first()
        self.assertTrue(subscription)   # subscription exists

    def test_notification(self):
        SubscriptionService.subscribe(self.postId, self.user2Id)

        with self.app as c:
            with c.session_transaction() as session:
                session["logged_in"] = self.user1Id
            self.app.post("/addComment/{}".format(self.postId), data={
                "body": "body"
            })
            notification = Notification.query.filter_by(title="New Comment")
            self.assertTrue(notification)  # notification exists


    def test_unsubscribe(self):
        SubscriptionService.subscribe(self.postId, self.user2Id)
        SubscriptionService.unsubscribe(self.postId, self.user2Id)
        subscription = Subscription.query.filter_by(post=self.postId).first()
        self.assertIsNone(subscription)  # subscription no longer exists

if __name__ == '__main__':
    unittest.main()
