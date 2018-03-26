from app.services.JsonService import JsonService
from app import socketio
import json


class NotificationService:
    @staticmethod
    def dispatch(notification):
        preppedNotification = JsonService.prepareModel(notification)
        data = json.dumps(preppedNotification)
        socketio.emit("NOTIFICATION-ADDED", data)
