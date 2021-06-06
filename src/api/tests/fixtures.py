import pytest

@pytest.fixture
def app():
    from flask import Flask
    from api import BASE_ROUTE as API_BASE_ROUTE
    from api.routes import api
    from api.course_types import BASE_ROUTE as COURSE_TYPES_BASE_ROUTE
    from api.course_types.routes import course_types
    app = Flask(__name__)
    app.register_blueprint(api, url_prefix=API_BASE_ROUTE)
    app.register_blueprint(course_types, url_prefix=API_BASE_ROUTE + COURSE_TYPES_BASE_ROUTE)
    yield app
 
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

