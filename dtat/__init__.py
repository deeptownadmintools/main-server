from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, upgrade
from sqlalchemy import MetaData
from dtat.basemodel import IdModel, naming_convention
import os


class DTAT(Flask):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @staticmethod
    def create_app():
        """
        Application factory
        """
        app = DTAT(__name__)

        app.config.from_object("dtat.defaultConfig")
        # try:
        #     app.config.from_object("dtat.privateConfig")
        # except ImportError:
        #     pass

        app.db = SQLAlchemy(app, model_class=IdModel,
                            metadata=MetaData(
                                naming_convention=naming_convention
                            ))

        migrate = Migrate(app, app.db, render_as_batch=True)  # noqa: F841

        return app

    def registerBlueprints(self):
        from dtat.api import homeprint
        self.register_blueprint(homeprint)

    def migrate_db(self):
        with self.app_context():
            path = os.path.dirname(os.path.abspath(__file__))
            upgrade(path + '/../migrations')


app = DTAT.create_app()
app.registerBlueprints()
app.migrate_db()

import dtat.models # noqa F402

__all__ = [
    'app'
]
