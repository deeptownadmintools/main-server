from dtat import DTAT
from flask_migrate import upgrade
import os
from pytest import fixture


@fixture(scope="session")
def app():
    app = DTAT.create_app("dtat.testConfig")

    with app.app_context():
        app.registerBlueprints()

    return app


@fixture(scope="session")
def db(app):
    with app.app_context():
        upgrade(os.path.dirname(__file__) + '/../migrations')
        app.db.create_all()
        app.db.session.expire_all()

    yield app.db

    with app.app_context():
        app.db.reflect()
        app.db.drop_all()
    os.unlink("/tmp/dtat_test")


@fixture(scope="session")
def client(app, db):
    client = app.test_client()

    return client
