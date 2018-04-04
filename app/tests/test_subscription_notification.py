from app.tests.base.BaseFixture import BaseFixture
from app.models.User import User
from app.models.Post import Post
from app.models.Comment import Comment
from app.models.Subscription import Subscription
from app.models.Notification import Notification
from app.services.SubscriptionService import SubscriptionService
from app.services.NotificationService import NotificationService

import unittest


class TestDiscussionGroups(BaseFixture):

    def setUp(self):
        super().setUp()
        user1 = User(username='user1', email='test@test.com', password='test')
        user2 = User(username='user2', email='test2@test.com', password='test')
        self.db.session.add(user1)
        self.db.session.add(user2)
        self.db.session.commit()
        self.user1Id = user1.id
        self.user2Id = user2.id


    def test_subscription(self):

        self.app.post("/postEdit", data={
            "title": "title",
            "body": "body",
            "poster_id": [self.userId],
        })

        post = Post.query.filter_by(title="title").first()
        SubscriptionService.subscribe(post.id, self.user2Id)
        subscription = Subscription.query.filter_by(postid=post.id)
        self.assertTrue(subscription)   # subscription exists
        SubscriptionService.unsubscribe(post.id, self.user2Id)
        subscription = Subscription.query.filter_by(postid=post.id)
        self.assertFalse(subscription)  # subscription no longer exists

    def test_notification(self):

        self.app.post("/postEdit", data={
            "title": "title",
            "body": "body",
            "poster_id": [self.userId],
        })

        post = Post.query.filter_by(title="title").first()
        SubscriptionService.subscribe(post.id, self.user2Id)
        subscription = Subscription.query.filter_by(postid=post.id)


        self.app.post("/addComment", data={
            "body": "body",
            "poster_id": [self.user1Id],
            "post_id": post.id
        })

        notification = Notification.query.filter_by(title="New Comment")
        self.assertTrue(notification)   # notification exists


    def test_unsubscribe(self):
        self.app.post("/postEdit", data={
            "title": "title",
            "body": "body",
            "poster_id": [self.userId],
        })

        post = Post.query.filter_by(title="title").first()
        SubscriptionService.subscribe(post.id, self.user2Id)
        SubscriptionService.unsubscribe(post.id, self.user2Id)
        subscription = Subscription.query.filter_by(postid=post.id)
        self.assertFalse(subscription)  # subscription no longer exists

if __name__ == '__main__':
    unittest.main()
