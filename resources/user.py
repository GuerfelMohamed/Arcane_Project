from flask_restful import Resource, reqparse
from flask_jwt import jwt_required, current_identity
from models.user import UserModel


class UserRegister(Resource):
    parser = reqparse.RequestParser()  # only allow price changes, no name changes allowed
    parser.add_argument('username', type=str, required=True, help='This field cannot be left blank')
    parser.add_argument('password', type=str, required=True, help='This field cannot be left blank')

    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'message': "User with {} has already been created, aborting.".format(data['username'])}, 400

        user = UserModel(**data)
        user.save_to_db()

        return {'message': 'user has been created successfully.'}, 201
    
    
class UserUpdate(Resource):
    parser = reqparse.RequestParser()  # only allow price changes, no name changes allowed
    parser.add_argument('username', type=str)
    parser.add_argument('password', type=str)

    @jwt_required()
    def put(self):
        user = UserModel.find_by_id(current_identity.id)
        data =UserUpdate.parser.parse_args()
        if data['username'] is not None:
            user.username = data['username']
        if data['password'] is not None:
            user.password = data['password']
        user.save_to_db()


