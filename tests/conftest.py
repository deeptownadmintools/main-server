from dtat import DTAT
from flask_migrate import upgrade
import os
from pytest import fixture


@fixture(scope="session")
def app(request):
    app = DTAT.create_app("dtat.testConfig")

    with app.app_context():
        app.registerBlueprints()

    return app


@fixture(scope="session")
def db(app, request):
    with app.app_context():
        upgrade(os.path.dirname(__file__) + '/../migrations')
        app.db.create_all()

    yield app.db

    with app.app_context():
        app.db.reflect()
        app.db.drop_all()
    os.unlink("/tmp/dtat_test")


@fixture(scope="session")
def client(app, db, request):
    client = app.test_client()

    return client


@fixture(scope='function')
def session(app, request):

    app.db.reflect()
    app.db.drop_all()
    app.db.create_all()

    yield app.db

    app.db.drop_all()
