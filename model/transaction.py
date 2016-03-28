from model.shared import db
import datetime

class transaction(db.Model):
    __tablename__ = 'item'

    id = db.Column(db.Integer, primary_key=True)
    client_id = db.Column(db.Integer, unique=True)
    item_id = db.Column(db.Integer)
    unit = db.Column(db.Integer)
    total = db.Column(db.Integer)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, client_id, price):
        #self.name = name
        #self.price = price
    
    @property
    def serialize(self):
      """Return object data in easily serializeable format"""
      return {
        'id': self.id,
        'name': self.name,
        'price': self.price
      }