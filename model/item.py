from model.shared import db
import datetime

class Item(db.Model):
    __tablename__ = 'item'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    price = db.Column(db.Integer)
    created = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    @property
    def serialize(self):
      """Return object data in easily serializeable format"""
      return {
        'id': self.id,
        'name': self.name,
        'price': self.price
      }