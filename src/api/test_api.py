from flask.testing import FlaskClient
from api.tests.fixtures import app, client

def test_empty_app(client):
    """Start with a blank database."""
    rv = client.get('/')
    assert b"Rigo welcomes you to your API!!" in rv.data
