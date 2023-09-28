"""file provided class-model for ORM"""
from __future__ import annotations
from passlib.hash import pbkdf2_sha256

from .db import db


class UserModel(db.Model):
    """class initialize table 'user' in database"""
    __tablename__ = "user"

    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String)
    password = db.Column(db.String)
    username = db.Column(db.String)

    def json(self) -> dict:
        """return public user data"""
        return {
            "id": self.id,
            "username": self.username
        }

    @classmethod
    def auth(cls, login: str, password: str) -> UserModel | None:
        """
        return user object or raise NotFound error
        
        :login:     login of user to retrieve
        :password:  password of user to retrieve
        """

        return cls.query.filter(
            cls.login == login,
            cls.password == pbkdf2_sha256.hash(password)
        ).one_or_none()

    @classmethod
    def get_by_id(cls, _id: int) -> UserModel | None:
        """
        method return user object with matching ID or None

        :id: user ID to retrieve
        """
        return cls.query.filter(cls.id == _id).one_or_none()

    def put(self, username: str =None, password: str =None) -> None:
        """
        modify user data fields

        :password:  new password
        :username:  new username
        """
        self.password = password or self.password
        self.username = username or self.username
