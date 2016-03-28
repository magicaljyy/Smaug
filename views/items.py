from flask import render_template, request
from forms import *
from flask_restful import Resource
from model.item import Item
from model.shared import db
from flask import jsonify

class ItemAPI(Resource):
  
  def get(self, item_id):
    item = Item.query.filter_by(id=item_id).first()
    return jsonify(json_list=[item.serialize])
  
  def post(self, item_id):
    item = Item.query.get(item_id)
    item.name = request.form['name']
    item.price = request.form['price']
    db.session.commit()
    return jsonify({'success':'1'})

class ItemListAPI (Resource):
  def get(self):
    items = Item.query.all()
    return jsonify(json_list=[i.serialize for i in items])
    
  def post(self):
    item = Item(**request.form)
    db.session.add(item)
    db.session.commit()
    return jsonify({'success':'1'})