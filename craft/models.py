from craft import db, login_manager,admin
from flask_login import UserMixin
from flask_admin.contrib.sqla import ModelView

@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(int(user_id)) #returning user with that id


class Users(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"Users('{self.username}', '{self.email}')"

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"Admin('{self.name}', '{self.email}')"

class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    picture = db.Column(db.String(60), nullable=False)
    description = db.Column(db.String(60), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"Products('{self.name}', '{self.price}','{self.picture}','{self.description}','{self.stock}','{self.category}')"

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    products_id = db.Column(db.Integer)
    users_id = db.Column(db.Integer)
    name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(60), nullable=False)
    address_line1 = db.Column(db.String(60), nullable=False)
    address_line2 = db.Column(db.String(60), nullable=False)
    pincode = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(60), nullable=False)
    state = db.Column(db.String(60), nullable=False)
    country = db.Column(db.String, nullable=False)
    mobile = db.Column(db.Integer, nullable=False)
    def __repr__(self):
        return f"Order('{self.products_id}','{self.users_id}','{self.name}', '{self.email}','{self.address_line1}','{self.address_line2}','{self.pincode}','{self.city},'{self.state},'{self.country},'{self.mobile}')"
       
admin.add_view(ModelView(Users,db.session))
admin.add_view(ModelView(Products,db.session))
admin.add_view(ModelView(Order,db.session))