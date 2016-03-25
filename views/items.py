from flask import render_template, request
from forms import *
from flask_restful import Resource
from model.item import Item

class ItemAPI(Resource):
  
  def get(self, item_id):
    if item_id == None:
      items = Item.query.all()
    else:
      item = Item.query.filter_by(id=item_id)
    return item_id
  
  def post(self, item_id):
    return request.form
    return item_id
    
  