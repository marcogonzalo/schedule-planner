# Main testing fila
# For more about Python/Flask testing
# see URL: https://flask.palletsprojects.com/en/2.0.x/testing/

import pytest

from app import app as _app
from api.db import db as _db
from api.models import *

@pytest.fixture(scope='module')
def app():
    _app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
    _app.config['TESTING'] = True
    return _app
 
@pytest.fixture(scope='module')
def client(app):
    with app.test_client() as client:
        _db.app = app
        _db.create_all()
        yield client
        _db.drop_all()

@pytest.fixture(scope='module')
def db(app):
    with app.app_context():
        _db.app = app
        _db.create_all()
        yield client
        _db.drop_all()
