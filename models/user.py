import sqlite3
from db import db

class UserModel(db.Model):
    __tablename__ = 'users'                             # table name config
    id = db.Column(db.Integer, primary_key = True)      # an primary key named id
    username = db.Column(db.String(80))                 # username field
    password = db.Column(db.String(80))                 # password field

    def __init__(self,username,password):
        self.username = username
        self.password = password


    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
