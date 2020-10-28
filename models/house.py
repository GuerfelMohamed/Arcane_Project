from db import db

class HouseModel(db.Model):
    __tablename__ = 'houses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    description = db.Column(db.String(1000))
    type_id = db.Column(db.Integer, db.ForeignKey('types.id'))
    city_id = db.Column(db.Integer, db.ForeignKey('cities.id'))
    rooms = db.relationship('RoomModel', lazy='dynamic')

    def __init__(self, name, description, type_id, city_id):
        self.name = name
        self.description = description
        self.type_id = type_id
        self.city_id = city_id

    def json(self):
        return {'id':self.id, 'name': self.name, 'description': self.description, 
                'House_type':self.type_id, 'city': self.city_id, 'rooms': [room.json() for room in self.rooms.all()]}

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()



# City Class/Model
class CityModel(db.Model):
    __tablename__ = 'cities'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    houses = db.relationship('HouseModel', uselist=False) #lazy='dynamic'

    def __init__(self,name):
        self.name

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()  

# Type of house Classs/Model

class TypeModel(db.Model):
    __tablename__ = 'types'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    houses = db.relationship('HouseModel', uselist=False) #lazy='dynamic'

    def __init__(self,name):
        self.name

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()  