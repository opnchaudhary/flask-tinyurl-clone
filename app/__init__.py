# coding:utf-8
import os

from flask import Flask, request, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from redis import StrictRedis
from config import Config

db = SQLAlchemy()
migrate = Migrate()
redis = StrictRedis(host='localhost', port=6379, db=0)

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app,db)


    from app.api import bp as api_bp
    app.register_blueprint(api_bp)

    from app.main import bp as main_bp
    app.register_blueprint(main_bp)

    #from app.errors import bp as error_bp
    #app.register_blueprint(error_bp)



    return app
