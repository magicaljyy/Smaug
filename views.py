from flask import render_template, request
from forms import *


def home():
    return render_template('pages/placeholder.home.html')

def about():
    return render_template('pages/placeholder.about.html')

def login():
    form = LoginForm(request.form)
    return render_template('forms/login.html', form=form)

def register():
    form = RegisterForm(request.form)
    return render_template('forms/register.html', form=form)

def forgot():
    form = ForgotForm(request.form)
    return render_template('forms/forgot.html', form=form)
    
# Test db
def testdb():
  if db.session.query("1").from_statement("SELECT 1").all():
      return 'It works.'
  else:
    return 'Something is broken.'