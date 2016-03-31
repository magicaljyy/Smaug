from flask_wtf import Form
from wtforms import TextField, PasswordField, FloatField
from wtforms.validators import DataRequired, EqualTo, Length
from model.user import User
# Set your classes here.


class RegisterForm(Form):
    name = TextField(
        'Username', validators=[DataRequired(), Length(min=6, max=25)]
    )
    email = TextField(
        'Email', validators=[DataRequired(), Length(min=6, max=40)]
    )
    password = PasswordField(
        'Password', validators=[DataRequired(), Length(min=6, max=40)]
    )
    confirm = PasswordField(
        'Repeat Password',
        [DataRequired(),
        EqualTo('password', message='Passwords must match')]
    )


class LoginForm(Form):
    email = TextField('Email', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])
    
    def __init__(self, *args, **kwargs):
      Form.__init__(self, *args, **kwargs)
      self.user = None
      
    def validate(self):
      user = User.query.filter_by(email=self.email.data).first()
      if user.password == self.password.data:
        self.user = user
        return True
      

class ForgotForm(Form):
    email = TextField(
        'Email', validators=[DataRequired(), Length(min=6, max=40)]
    )

class AddBalanceForm(Form):
    amount = FloatField(
        'Amount', validators=[DataRequired()]
    )
    def validate(self):
     return self.amount.data

class AddItemForm(Form):
    name = TextField(
        'Name', validators=[DataRequired()]
    )
    price = FloatField(
        'Price', validators=[DataRequired()]
    )
    def validate(self):
     return self.name.data and self.price.data
