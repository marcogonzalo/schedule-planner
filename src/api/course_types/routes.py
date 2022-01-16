from flask import Blueprint, jsonify, request
from .model import CourseType

course_types = Blueprint('course_types', __name__)


@course_types.route('')
def index():
    course_types = CourseType.query.all()
    course_type_list = []
    for course_type in course_types:
        course_type_list.append(course_type.to_dict())
    return jsonify(course_type_list), 200


@course_types.route('', methods=['POST'])
def create():
    body = request.get_json()
    if body is None:
        return "The request body is null", 400
    
    name = body.get('name', None)
    if name is None or len(name) == 0:
        return "Please, provide a valid CourseType name", 422

    duration = int(body.get('duration', '0'))
    if duration is None or duration <= 0:
        return "Please, provide a valid CourseType duration", 422

    course_type = CourseType(name=name, duration=duration)
    course_type.create()

    return "Course type created", 201


@course_types.route('/<int:id>')
def show(id):
    course_type = CourseType.get_by_id(id)
    return jsonify(course_type.to_dict()), 200


@course_types.route('/<int:id>', methods=['PUT'])
def update(id):
    body = request.get_json()
    if body is None:
        return "The request body is null", 400

    course_type = CourseType.get_by_id(id)

    data = {
        'name': body.get('name', None),
        'duration': int(body.get('duration', '0')),
    }
    
    if data['name'] is None or len(data['name']) == 0:
        return "Please, provide a valid CourseType name", 422

    if data['duration'] is None or data['duration'] <= 0:
        return "Please, provide a valid CourseType duration", 422

    course_type.update(**data)
    return jsonify(course_type.to_dict()), 200

@course_types.route('/<int:id>', methods=['DELETE'])
def delete(id):
    course_type = CourseType.get_by_id(id)
    course_type.delete()
    return "Course Type deleted", 205
