from flask.testing import FlaskClient
from api.tests import API_BASE_URL
from api.tests.fixtures import app, client
from . import BASE_ROUTE
from .model import CourseType

URL = API_BASE_URL + BASE_ROUTE


# Helper methods
def make_course_type(id: int = 123, name: str = 'Test CourseType',
                duration: int = 1) -> CourseType:
    return CourseType(id=id, name='Test CourseType {}'.format(id), duration=duration)


def get_course_type(client, id):
    return client.get("{url}/{id}".format(url=URL, id=id))


def get_course_types(client):
    return client.get(URL)


def create_course_type(client, payload):
    return client.post(URL, json=payload, follow_redirects=True)


def update_course_type(client, id, payload):
    return client.put("{url}/{id}".format(url=URL, id=id), json=payload, follow_redirects=True)


def delete_course_type(client, id):
    return client.delete("{url}/{id}".format(url=URL, id=id))


class TestCourseTypeResource:
    def test_create(self, client):
        course_type = make_course_type()
        payload = dict(name=course_type.name, duration=course_type.duration)
        response = create_course_type(client, payload)
        assert response._status_code == 201

    def test_create_with_invalid_data(self, client):
        course_type = make_course_type()
        payload = None
        response = create_course_type(client, payload)
        assert response._status_code == 400
        assert b'The request body is null' in response.data

        payload = dict(duration=course_type.duration)
        response = create_course_type(client, payload)
        assert response._status_code == 422
        assert b'Please, provide a valid CourseType name' in response.data

        payload = dict(name='', duration=course_type.duration)
        response = create_course_type(client, payload)
        assert response._status_code == 422
        assert b'Please, provide a valid CourseType name' in response.data

        payload = dict(name=course_type.name)
        response = create_course_type(client, payload)
        assert response._status_code == 422
        assert b'Please, provide a valid CourseType duration' in response.data

        payload = dict(name=course_type.name,
                       duration=-course_type.duration)
        response = create_course_type(client, payload)
        assert response._status_code == 422
        assert b'Please, provide a valid CourseType duration' in response.data

    def test_show(self, client):
        course_type = make_course_type(id=1)
        response = get_course_type(client, course_type.id)
        assert response._status_code == 200
        assert response.json.get('id') == course_type.id

    def test_update_with_invalid_data(self, client):
        course_type = make_course_type(id=1)
        new_duration = course_type.duration + 1

        payload = None
        response = update_course_type(client, course_type.id, payload)
        assert response._status_code == 400
        assert b'The request body is null' in response.data

        payload = dict(duration=course_type.duration)
        response = update_course_type(client, course_type.id, payload)
        assert response._status_code == 422
        assert b'Please, provide a valid CourseType name' in response.data

        payload = dict(name='', duration=course_type.duration)
        response = update_course_type(client, course_type.id, payload)
        assert response._status_code == 422
        assert b'Please, provide a valid CourseType name' in response.data

        payload = dict(name=course_type.name)
        response = update_course_type(client, course_type.id, payload)
        assert response._status_code == 422
        assert b'Please, provide a valid CourseType duration' in response.data

        payload = dict(name=course_type.name,
                       duration=-course_type.duration)
        response = update_course_type(client, course_type.id, payload)
        assert response._status_code == 422
        assert b'Please, provide a valid CourseType duration' in response.data

    def test_update(self, client):
        course_type = make_course_type(id=1)
        new_duration = course_type.duration + 1

        payload = dict(name=course_type.name, duration=new_duration)
        response = update_course_type(client, course_type.id, payload)
        assert response._status_code == 200
        assert response.json.get('duration') == new_duration

    def test_index(self, client):
        for i in range(12, 15):
            course_type = make_course_type(id=i)
            course_type.create()
        response = get_course_types(client)
        assert response._status_code == 200
        assert len(response.get_json()) > 1

    def test_delete(self, client):
        course_type = make_course_type(id=1)
        response = delete_course_type(client, course_type.id)
        assert response._status_code == 205

    """
    @patch.object(WidgetService, 'get_all',
                  lambda: [make_widget(123, name='Test Widget 1'),
                           make_widget(456, name='Test Widget 2')])
    def test_get(self, client: FlaskClient):  # noqa
        with client:
            results = client.get(API_BASE_ROUTE + BASE_ROUTE,
                                 follow_redirects=True).get_json()
            expected = WidgetSchema(many=True).dump(
                [make_widget(123, name='Test Widget 1'),
                 make_widget(456, name='Test Widget 2')]
            ).data
            for r in results:
                assert r in expected
    """
