from db import db


class RoomModel(db.Model):
    __tablename__ = 'rooms'

    id = db.Column(db.Integer, primary_key=True)
    characteristics = db.Column(db.String(1000))
    house_id = db.Column(db.Integer, db.ForeignKey('houses.id'))
    #house = db.relationship('HouseModel')


    def __init__(self, characteristics, house_id):
        self.characteristics = characteristics
        self.house_id = house_id

    def json(self):
        return {'id': self.id, 'characteristics': self.characteristics, 'house_id': self.house_id}

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()  

    def save_to_db(self):  
        db.session.add(self)
        db.session.commit()  

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
