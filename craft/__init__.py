from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.secret_key = 'hello'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app) #passing app to bcrypt,so as to initialize that
login_manager = LoginManager(app) #creating an instance of loginmanager
login_manager.login_view = 'login' #login is the function name of route, telling to login first before accessing prdt list

from craft import routes