from model.shared import db
import datetime

class User(db.Model):
  __tablename__ = 'user'

  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(120), unique=True)
  password = db.Column(db.String(30))
  balance = db.Column(db.Float(30))
  created = db.Column(db.DateTime)

  def __init__(self, email=None, password=None):
    self.email = email
    self.password = password