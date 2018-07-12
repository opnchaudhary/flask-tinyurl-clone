# coding:utf-8
import os

from flask import Flask, request, current_app
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_migrate import Migrate
from flask_moment import Moment
from config import Config

bcrypt = Bcrypt()
db = SQLAlchemy()
migrate = Migrate()
moment = Moment()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.login_message='Please login to access this page'
mail = Mail()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    bcrypt.init_app(app)
    db.init_app(app)
    migrate.init_app(app,db)
    moment.init_app(app)
    login_manager.init_app(app)


    from app.api import bp as api_bp
    app.register_blueprint(api_bp)
    #from app.errors import bp as error_bp
    #app.register_blueprint(error_bp)



    return app
