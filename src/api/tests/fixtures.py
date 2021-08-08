# Main testing fila
# For more about Python/Flask testing
# see URL: https://flask.palletsprojects.com/en/2.0.x/testing/

import os
import tempfile
import pytest
from flask import Flask
from flask_migrate import Migrate
from app import app as _app
from api.db import db as _db
from api.routes import api

@pytest.fixture
def app():
    _app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////tmp/test.db"
    _app.config['TESTING'] = True
    yield _app
 
@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client

@pytest.fixture
def db(app):
   with app.app_context():
        _db.create_all()
        yield _db
        _db.drop_all()
        _db.session.commit()
