from model.shared import db

class Item(db.Model):
    __tablename__ = 'item'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True)
    price = db.Column(db.Integer)
    created = db.Column(db.DateTime)

    def __init__(self, name, price):
        self.name = name
        self.price = price