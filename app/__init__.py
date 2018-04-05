from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_socketio import SocketIO

from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
socketio = SocketIO(app)

from app import routes
from app.modelsImport import *

if __name__ == "__main__":
    socketio.run(app)
