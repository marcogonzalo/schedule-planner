from ..db import db

class CourseType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    duration = db.Column(db.Integer, unique=True, nullable=False)

    def __repr__(self):
        return '<CourseType: %r>' % self.name

    def create(self):
        db.session.add(self)
        db.session.commit()

    def serialize(self):
        return {
            "name": self.name,
            "duration": self.duration
        }
