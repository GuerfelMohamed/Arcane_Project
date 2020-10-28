from flask_restful import Resource, reqparse
from models.house import HouseModel, CityModel, TypeModel
from models.room import RoomModel
import ast

class House(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str)
    parser.add_argument('description', type=str)
    parser.add_argument('house_type', type=str)
    parser.add_argument('city', type=str)

    def get(self, id):
        house = HouseModel.find_by_id(id)
        if house:
            return house.json()
        return {'message': 'house not found'}, 404

    def delete(self, id):
        house = HouseModel.find_by_id(id)
        if house:
            house.delete_from_db()

        return {'message': 'house deleted'}
    
    def put(self, id):
        house = HouseModel.find_by_id(id)
        if not house:
            return {'message': 'house not found'}, 404
        data = House.parser.parse_args()
        if data['name'] is not None:
            house.name = data['name']
        if data['description'] is not None:
            house.description = data['description']
        if data['house_type'] is not None:
            house_type = TypeModel.find_by_name(data['house_type'])
            if not house_type:
                return {'message':"invalide house type"}, 400
            house.type_id = house_type.id
        if data['city'] is not None:
            city = CityModel.find_by_name(data['city'])
            if not city:
                return {'message':"invalide city name"}, 400
            house.city_id = city.id

        house.save_to_db()
        house.json()


        
            



class AddHouse(Resource):
        parser = reqparse.RequestParser() 
        parser.add_argument('name', type=str, required=True, help='Must enter the house name')
        parser.add_argument('description', type=str)
        parser.add_argument('house_type', type=str, required=True, help='Must enter the house type')
        parser.add_argument('city', type=str, required=True, help='Must enter the house location')
        parser.add_argument('rooms',type=str, action="append")
        
        def post(self):
            data = AddHouse.parser.parse_args()

            house_type = TypeModel.find_by_name(data['house_type'])
            if not house_type:
                return {'message':"invalide house type"}, 400

            city = CityModel.find_by_name(data['city'])
            if not city:
                return {'message':"invalide city name"}, 400
            
                
            house = HouseModel(data['name'],data['description'],house_type.id,city.id)
            try:
                house.save_to_db()
            except:
                return {"message": "An error occurred creating the store."}, 500
            
            # add the new house attached rooms
            if data['rooms'] is not None:
                rooms =[ast.literal_eval(rooms) for rooms in data['rooms']]
                for x in rooms:
                    room = RoomModel(x['characteristics'],house.id)
                    room.save_to_db()

            return house.json(), 201

class HouseList(Resource):
    def get(self,city):
        city= CityModel.find_by_name(city)
        return {'houses': [house.json() for house in HouseModel.query.filter_by(city_id=city.id).all()]}