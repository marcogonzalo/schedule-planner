from ..db import db

class CourseType(db.Model):
    __tablename__ = "course_types"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    duration = db.Column(db.Integer, unique=True, nullable=False)

    def __repr__(self):
        return "<CourseType: {name}>".format(self.name)

    def create(self):
        db.session.add(self)
        db.session.commit()

    # serialize object
    def to_dict(self):
        return {
            "name": self.name,
            "duration": self.duration
        }
