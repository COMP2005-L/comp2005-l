from app.models.Subscription import Subscription
from app import db


class SubscriptionService:

    @staticmethod
    def isSubscribed(postId, userId):
        """
        Checks if the given user is subscribed to the provided post

        :param postId: int - The id of the post to check subscription against
        :param userId: int - The id of the user to be checked as a subscriber
        :return: Subscription|None
        """
        subscription = Subscription.query.filter(Subscription.post == postId, Subscription.subscriber == userId).first()
        return subscription

    @staticmethod
    def getSubscriptions(postId):
        """
        Returns a list of all the subscribers for a given post

        :param postId: int - The id of the post to retrieve subscribers for
        :return: list<Subscription>
        """
        return Subscription.query.filter_by(post=postId).all()

    @staticmethod
    def subscribe(postId, userId):
        """
        Subscribe the given user to the provided post, if the user is not already subscribed

        :param postId: int - The id of the post to be subscribed to
        :param userId: int - The id of the new subscriber
        :raises ValueError
        :return: None
        """
        if (SubscriptionService.isSubscribed(postId, userId)):
            raise ValueError("Already subscribed!")

        subscription = Subscription(post=postId, subscriber=userId)
        db.session.add(subscription)
        db.session.commit()

    @staticmethod
    def unsubscribe(postId, userId):
        """
        Unsubscribe the given user from the provided post, if the user is already subscribed

        :param postId: int - The id of the post to be unsubscribed from
        :param userId: int - The id of the subscriber to be unsubscribed
        :raises ValueError
        :return: None
        """
        if (not SubscriptionService.isSubscribed(postId, userId)):
            raise ValueError("Already unsubscribed!")

        subscription = Subscription.query.filter(Subscription.post == postId, Subscription.subscriber == userId).first()
        db.session.delete(subscription)
        db.session.commit()
