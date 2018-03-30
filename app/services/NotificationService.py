from app.services.JsonService import JsonService
from app import socketio
import json


class NotificationService:
    """
    Notification service takes care of handling some common functions tied to notifications, like
    dispatching.

    Methods:
        dispatch
    """
    @staticmethod
    def dispatch(notification):
        """
       Fires a socket event containing a serialized form of the provided notification

       Examples:
           - To dispatch a notification
               notification = Notification(...)
               NotificationService.dispatch(notification)

       :param instance: Notification
       :return: None
        """
        preppedNotification = JsonService.prepareModel(notification)
        data = json.dumps(preppedNotification)
        socketio.emit("NOTIFICATION-ADDED", data)
