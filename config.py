# coding:utf-8
import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or '89201ee95a4ca4cd1f376eb58e0fa10f'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgres://flaskmovie:flaskmovie@localhost/tinyurl'
    ADMINS = ['opnchaudhary@gmail.com']
    LANGUAGES = ['en']
    POSTS_PER_PAGE = 25
    DEBUG = True
