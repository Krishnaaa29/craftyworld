from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FileField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from craft.models import Users,Products,Order

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('SignUp')

    def validate_username(self, username):
        user = Users.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('This username is taken, please choose a different one')

    def validate_email(self, email):
            user = Users.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('This email is taken, please choose a different one')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username: #checks whether given username is diffrt from already entered one(to update properly)
            user = Users.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('This username is taken, please choose a different one')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = Users.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('This email is taken, please choose a different one')

class ProductsForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])
    price = StringField('Price', validators=[DataRequired()])
    picture = FileField('Picture', validators=[FileAllowed('jpg','png'), FileRequired('choose a file!')])
    description = StringField('Description', validators=[DataRequired(), Length(min=2, max=20)])
    stock = StringField('Stock', validators=[DataRequired()])
    category = StringField('Category', validators=[DataRequired(), Length(min=2, max=20)])
    
    submit = SubmitField('Add')
    
    

    def validate_name(self, name):
        product = Products.query.filter_by(name=name.data).first()
        if product:
            raise ValidationError('This name is taken, please choose a different one')

class OrderForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    address_line1 = StringField('Address_line1', validators=[DataRequired(), Length(min=2, max=20)])
    address_line2 = StringField('Address_line2', validators=[DataRequired(), Length(min=2, max=20)])
    pincode = StringField('Pincode', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    country = StringField('Country', validators=[DataRequired()])
    mobile = StringField('Mobile', validators=[DataRequired(),Length(min=10, max=12)])

    submit = SubmitField('Order')
    




