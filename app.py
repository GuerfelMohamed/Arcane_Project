from flask import Flask
from flask_restful import Api

from db import db 
from config import mysqlConfig
from resources.room import Room, RoomList
from resources.house import HouseList, AddHouse, House

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = mysqlConfig
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)



api.add_resource(HouseList, '/houses/<string:city>')
api.add_resource(AddHouse, '/addHouse')
api.add_resource(House, '/house/<int:id>')
api.add_resource(RoomList, '/rooms/<int:house_id>')
api.add_resource(Room, '/room/<int:id>')

with app.app_context():
    db.init_app(app)
    db.create_all()
