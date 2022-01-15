from flask import Blueprint, request
from .model import CourseType

course_types = Blueprint('course_types', __name__)

@course_types.route('', defaults={'page': 'index'})
def index():
    return "Course Type List", 200

@course_types.route('/<course_type>')
def show():
    return "Course Type View", 200

@course_types.route('', methods=['POST'])
def create():
    body = request.get_json()
    if body is None:
        return "The request body is null", 400
    
    name = body.get('name')
    if name is None or len(name) == 0:
        return "Please, provide a valid CourseType name", 422

    duration = body.get('duration')
    if duration is None or duration <= 0:
        return "Please, provide a valid CourseType duration", 422

    course_type = CourseType(name=name, duration=duration)
    course_type.create()

    return "Created", 201