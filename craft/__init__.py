import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

import os.path as op
from craft.config import Config

app = Flask(__name__)
app.config.from_object(Config)

app.secret_key = 'hello'

db = SQLAlchemy(app)



file_path = op.join(op.dirname(__file__), 'static/productpic')
try:
    os.mkdir(file_path)
except OSError:
    pass

bcrypt = Bcrypt(app) #passing app to bcrypt,so as to initialize that
login_manager = LoginManager(app) #creating an instance of loginmanager
login_manager.login_view = 'user.login' #login is the function name of route, telling to login first before accessing prdt list
login_manager.login_message_category = 'info'

from craft.user.routes import user
from craft.product.routes import product
from craft.orders.routes import orders
from craft.main.routes import main

app.register_blueprint(user)
app.register_blueprint(product)
app.register_blueprint(orders)
app.register_blueprint(main)

from craft import route