from pytest import fixture
from .model import CourseType

@fixture
def course_type() -> CourseType:
    return CourseType(id=1, name='Test-CourseType-1', duration=45)

def test_course_type_create(course_type: CourseType):
    assert course_type
