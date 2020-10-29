from flask import Flask
from flask_jwt import JWT
from flask_restful import Api

from db import db 
from config import mysqlConfig
from resources.room import Room, RoomList
from resources.house import HouseList, AddHouse, House
from resources.user import UserRegister, UserUpdate
from security import authenticate, identity

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = mysqlConfig
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'Dese.Decent.Pups.BOOYO0OST'
api = Api(app)


jwt = JWT(app, authenticate, identity) #Auto Creates /auth endpoint
api.add_resource(UserRegister,'/register') #register user
api.add_resource(UserUpdate, '/update') # update user info
api.add_resource(HouseList, '/houses/<string:city>') # find houses by city
api.add_resource(AddHouse, '/addHouse') # add new house
api.add_resource(House, '/house/<int:id>') # update/delete house
api.add_resource(RoomList, '/rooms/<int:house_id>') # get house rooms
api.add_resource(Room, '/room/<int:id>') # update/delete room

with app.app_context():
    db.init_app(app)
    db.create_all()
