from craft import db, login_manager, app
from flask_login import UserMixin


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
    image_file = db.Column(db.String(60), nullable=False)
    description = db.Column(db.String(60), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    Orders = db.relationship('Order', backref='Products', lazy=True)

    def __repr__(self):
        return f"Products('{self.name}', '{self.price}','{self.image_file}','{self.description}','{self.stock}')"

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    products_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    users_id = db.Column(db.Integer)
    name = db.Column(db.String(60), nullable=False)
    address = db.Column(db.String(60), nullable=False)
    pincode = db.Column(db.Integer, nullable=False)
    city = db.Column(db.String(60), nullable=False)
    state = db.Column(db.String(60), nullable=False)
    mobile = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(60), nullable=False)
    def __repr__(self):
        return f"Order('{self.products_id}','{self.users_id}','{self.name}','{self.address}','{self.pincode}','{self.city},'{self.state},'{self.mobile}','{self.status}')"
       

class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(60), nullable=False)
    message = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"Feedback('{self.name}', '{self.email}', '{self.message}')"


