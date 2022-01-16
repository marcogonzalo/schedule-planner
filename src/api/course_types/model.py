from ..db import db

class CourseType(db.Model):
    __tablename__ = "course_types"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, unique=True, nullable=False)
    duration = db.Column(db.Integer, unique=False, nullable=False)

    def __repr__(self):
        return "<CourseType: {name}>".format(self.name)

    @classmethod
    def get_by_id(cls, id):
        element = cls.query.get(id)
        return element

    def create(self):
        db.session.add(self)
        db.session.commit()

    def update(self, **kwargs):
        for key, value in kwargs.items():
            if value is not None:
                setattr(self, key, value)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    # serialize object
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "duration": self.duration
        }
