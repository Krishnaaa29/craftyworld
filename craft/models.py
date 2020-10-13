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
    description = db.Column(db.String(60), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"Products('{self.name}', '{self.price}','{self.description}','{self.stock}','{self.category}')"
       
admin.add_view(ModelView(Users,db.session))
admin.add_view(ModelView(Products,db.session))