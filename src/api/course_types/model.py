from ..db import db

class CourseType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)
    duration = db.Column(db.Integer, unique=True)

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
