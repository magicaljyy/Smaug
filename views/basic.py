from flask import render_template, request, flash, session, url_for, redirect
from forms import *
import requests
from model.item import Item
from model.user import User
from model.shared import db

def home():
  if 'user_id' in session:
    items = Item.query.all()
    user = User.query.filter_by(id=session['user_id']).first()
    form = AddBalanceForm(request.form)
    if form.validate_on_submit():
      user.balance += form.amount.data
      flash(u'Successfully added %d' % form.amount.data)
      db.session.commit()
      return redirect(url_for('home'))
    add_item_form = AddItemForm(request.form)
    if add_item_form.validate_on_submit():
      item = Item(add_item_form.name.data, add_item_form.price.data)
      db.session.add(item)
      db.session.commit()
      flash(u'Successfully added %s for price %d' % (add_item_form.name.data, add_item_form.price.data))
      return redirect(url_for('home'))
    return render_template('pages/placeholder.home.html', items=items, user=user, form=form, add_item_form=add_item_form)
  return render_template('pages/non_login.html')

def about():
  return render_template('pages/placeholder.about.html')

def login():
  form = LoginForm(request.form)
  if form.validate_on_submit():
    flash(u'Successfully logged in as %s' % form.user.email)
    session['user_id'] = form.user.id
    return redirect(url_for('home'))
  return render_template('forms/login.html', form=form)

def register():
  form = RegisterForm(request.form)
  return render_template('forms/register.html', form=form)

def forgot():
  form = ForgotForm(request.form)
  return render_template('forms/forgot.html', form=form)

def logout():
  session.clear()
  return redirect(url_for('home'))
    
# Test db
def testdb():
  if db.session.query("1").from_statement("SELECT 1").all():
    return 'It works.'
  else:
    return 'Something is broken.'

def add_balance():
  return
