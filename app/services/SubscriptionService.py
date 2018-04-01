from app.models.Subscription import Subscription
from app import db


class SubscriptionService:

    @staticmethod
    def isSubscribed(postId, userId):
        subscription = Subscription.query.filter(Subscription.post == postId, Subscription.subscriber == userId).first()
        return subscription

    @staticmethod
    def getSubscriptions(postId):
        return Subscription.query.filter_by(post=postId).all()

    @staticmethod
    def subscribe(postId, userId):
        if (SubscriptionService.isSubscribed(postId, userId)):
            raise ValueError("Already subscribed!")

        subscription = Subscription(post=postId, subscriber=userId)
        db.session.add(subscription)
        db.session.commit()

    @staticmethod
    def unsubscribe(postId, userId):
        if (not SubscriptionService.isSubscribed(postId, userId)):
            raise ValueError("Already unsubscribed!")

        subscription = Subscription.query.filter(Subscription.post == postId, Subscription.subscriber == userId).first()
        db.session.delete(subscription)
        db.session.commit()
