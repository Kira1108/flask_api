# import sqlite3
from db import db

class StoreModel(db.Model):

    '''
        Everything looks the same as ItemModel
        Except:
            1. The constructor only contains 1 parameters
            which is name
            2. The json method returns name and items,
            we have to find these items.
    '''

    __tablename__='stores'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(80))

    # Note: this is an one-to-many relationship
    # so items is a list of items
    items = db.relationship('ItemModel', lazy = 'dynamic')


    def __init__(self, name):
         self.name = name

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name = name).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def json(self):
        # when we use laze = dynamic, the
        return {'name':self.name,"items":[item.json() for item in self.items.all()]}
