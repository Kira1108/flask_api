from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.store import StoreModel

class Store(Resource):

    def post(self,name):

        store = StoreModel.find_by_name(name)
        if store:
            return {"message":"A store with name {} already exists".format(name)},400

        store = StoreModel(name)

        try:
            store.save_to_db()
        except:
            return {"message":"An error occured while creating store"},500

        return store.json(), 201


    def delete(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            try:
                store.delete_from_db()
            except:
                return {'message':'An error occured while deleting store'},500
        return {"message":'store {} already deleted.'.format(name)}

    def get(self,name):
        store = StoreModel.find_by_name(name)
        if store:
            return store.json(), 200
        return {'message':"Store with name {} can not be found".format(name)},404

class StoreList(Resource):
    def get(self):
        return {"stores":[store.json() for store in StoreModel.query.all()]},200
