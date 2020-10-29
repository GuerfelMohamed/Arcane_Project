from flask_restful import Resource, reqparse
from models.room import RoomModel


class Room(Resource):
    parser = reqparse.RequestParser()  
    parser.add_argument('characteristics', type=str, required=True, help='Must enter the room characteristics')



    """def post(self, id):
        if RoomModel.find_by_name(name):
            return {'message': "A room with name '{}' already exists.".format(name)}, 400

        data = Room.parser.parse_args()
        room = RoomModel(name, data['characteristics'], data['house_id'])

        try:
            room.save_to_db()
        except:
            return {"message": "An error occurred inserting the room."}, 500
        return room.json(), 201"""

    #@jwt_required()
    def delete(self, id):

        room = RoomModel.find_by_id(id)
        if room:
            room.delete_from_db()
            return {'message': 'room has been deleted'}

    #@jwt_required()
    def put(self, id):
        room = RoomModel.find_by_id(id)
        if not room:
            return {'message': 'room not found'}
        data = Room.parser.parse_args()
        room.characteristics = data['characteristics']

        room.save_to_db()
        return room.json()


class RoomList(Resource):
    def get(self,house_id):
        return {'rooms': [room.json() for room in RoomModel.query.filter_by(house_id=house_id).all()]}
