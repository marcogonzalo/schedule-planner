from flask.testing import FlaskClient
from api.tests import API_BASE_URL
from api.tests.fixtures import client, app
from . import BASE_ROUTE
from .model import CourseType

URL = API_BASE_URL + BASE_ROUTE

def make_course_type(id: int = 123, name: str = 'Test CourseType',
                duration: int = 1) -> CourseType:
    return CourseType(id=id, name=name, duration=duration)

def create_course_type(client, payload):
    return client.post(URL, json=payload, follow_redirects=True)

# class TestCourseTypeResource:
#     def test_create(self, client):
#         course_type = make_course_type()
#         payload = dict(
#             name=course_type.name,
#             duration=course_type.duration
#         )
#         response = create_course_type(client, payload)
#         print("--------response",response.__dict__)
#         assert response._status_code == 201

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
