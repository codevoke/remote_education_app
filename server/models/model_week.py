"""file provided class-model for ORM"""
from __future__ import annotations

from .db import db


class WeekModel(db.Model):
    """class initialize table 'week' in database"""
    __tablename__ = 'week'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def json(self) -> dict:
        """return week json data"""
        return {
            "id": self.id,
            "name": self.name,
            "data": [
                day.json() for day in self.days
            ]
        }

    @classmethod
    def get_by_id(cls, _id: int) -> WeekModel | None:
        """
        method return week object with matching ID or None

        :_id: ID for retrieve
        """
        return cls.query.filter(cls.id == _id).one_or_none()
