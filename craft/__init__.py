import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_admin import Admin
import os.path as op

app = Flask(__name__)
app.secret_key = 'hello'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)

admin = Admin(app) 

file_path = op.join(op.dirname(__file__), 'static/productpic')
try:
    os.mkdir(file_path)
except OSError:
    pass

bcrypt = Bcrypt(app) #passing app to bcrypt,so as to initialize that
login_manager = LoginManager(app) #creating an instance of loginmanager
login_manager.login_view = 'login' #login is the function name of route, telling to login first before accessing prdt list
login_manager.login_message_category = 'info'

from craft import routes