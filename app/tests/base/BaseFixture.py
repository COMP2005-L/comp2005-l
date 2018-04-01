import unittest
import tempfile
import os

from config import basedir
from app import app
from flask_sqlalchemy import SQLAlchemy


class BaseFixture(unittest.TestCase):

    def setUp(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        app.testing = True
        app.db = SQLAlchemy(app)
        self.app = app.test_client()
        self.db = app.db

    def tearDown(self):
        # clear the test database's tables by deleting all records
        import inspect
        from app import modelsImport
        models = [cls for cls in modelsImport.__dict__.values() if inspect.isclass(cls)]
        for model in models:
            app.db.session.query(model).delete()

        app.db.session.commit()
        app.db.session.remove()


if __name__ == '__main__':
    unittest.main()
