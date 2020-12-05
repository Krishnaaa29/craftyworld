from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from flask_login import current_user
from wtforms import StringField, SubmitField, FileField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from craft.models import Products


class ProductsForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=20)])
    price = StringField('Price', validators=[DataRequired()])
    image_file = FileField('Picture', validators=[FileAllowed('jpg','png'), FileRequired('choose a file!')])
    description = StringField('Description', validators=[DataRequired(), Length(min=2, max=20)])
    stock = StringField('Stock', validators=[DataRequired()])
    
    submit = SubmitField('Add')
    
    

    def validate_name(self, name):
        product = Products.query.filter_by(name=name.data).first()
        if product:
            raise ValidationError('This name is taken, please choose a different one')
