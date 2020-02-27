import sqlite3
from flask_restful import Resource,reqparse
from models.user import UserModel

class UserRegister(Resource):

    # initialize a parser
    parser = reqparse.RequestParser()

    # add arguments username and password
    parser.add_argument('username',
    type = str,
    required=True,
    help = 'This filed can not be left blank')

    parser.add_argument('password',
    type = str,
    required=True,
    help = 'This filed can not be left blank')


    def post(self):

        # retrieve the payload
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'message':"A user with name {} already exists".format(data['username'])},400


        user = UserModel(**data)

        try:
            user.save_to_db()
        except:
            return {'message':'An error occured while register.'}

        return {'message':'User created successful.'},201
