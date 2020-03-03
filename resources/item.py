import sqlite3
from flask_restful import reqparse, Resource
from flask_jwt import jwt_required
from models.item import ItemModel


class Item(Resource):

    parser = reqparse.RequestParser()

    parser.add_argument('price',    # field name accepted
    type=float,                     # data type of the field
    required=True,                  # this field has to be in the json payload
    help = 'This field can not be left blank!' # missing field help info
    )

    parser.add_argument('store_id',    # field name accepted
    type=int,                     # data type of the field
    required=True,                  # this field has to be in the json payload
    help = 'Every Item needs a store id!' # missing field help info
    )

    @jwt_required() # we are going to authenticate before we call get method.
    def get(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json(), 200
        return {"message":'Item not exist.'}, 400

    def post(self,name,store_id):
        if ItemModel.find_by_name(name):
            return {'message':'item already exists.'},400
        data = Item.parser.parse_args()
        item = ItemModel(name,**data)
        try:
            item.save_to_db()
        except:
            return {'message':"An error occurred while insertion"},500
        return {'item':item.json()},201

    def delete(self,name):
        item = ItemModel.find_by_name(name)
        if item:
            try:
                item.delete_from_db()
            except:
                return {"message":"An error occured during deleting data."}
        return {"message":'Item has beed deleted.'}

    def put(self,name):
        data = Item.parser.parse_args()
        item = ItemModel.find_by_name(name)
        if item is None:
            item = ItemModel(name, **data)
        else:
            item.price = data['price']
            item.store_id = data['store_id']
        item.save_to_db()
        return item.json(), 200

class Itemlist(Resource):
    def get(self):
        return {'items':[item.json() for item in ItemModel.query.all()]}
