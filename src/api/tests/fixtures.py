# Main testing fila
# For more about Python/Flask testing
# see URL: https://flask.palletsprojects.com/en/2.0.x/testing/

import pytest
from flask import Flask
from app import app as application

@pytest.fixture
def app():
    yield application
 
@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client

@pytest.fixture
def db(app):
    from app import db
    with app.app_context():
        db.create_all()
        yield db
        db.drop_all()
        db.session.commit()

