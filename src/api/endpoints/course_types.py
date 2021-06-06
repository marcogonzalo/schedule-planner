from flask import Blueprint

course_types = Blueprint('course_types', __name__)

@course_types.route('/', defaults={'page': 'index'})
def index():
    return "Course Type List", 200

@course_types.route('/<course_type>')
def show():
    return "Course Type View", 200