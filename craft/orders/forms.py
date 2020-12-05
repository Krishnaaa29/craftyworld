from flask_wtf import FlaskForm
from flask_login import current_user
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from craft.models import Order





class OrderForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])
    address = StringField('Address', validators=[DataRequired(), Length(min=2, max=20)])
    pincode = StringField('Pincode', validators=[DataRequired()])
    city = StringField('City', validators=[DataRequired()])
    state = StringField('State', validators=[DataRequired()])
    mobile = StringField('Mobile', validators=[DataRequired(),Length(min=10, max=12)])
    status = HiddenField(default='Order Placed')
    submit = SubmitField('Order')
    




