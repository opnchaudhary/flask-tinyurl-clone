# coding:utf-8
from app import db

class Url(db.Model):
    key = db.Column(db.String(7), primary_key=True)
    value = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<Url {}>'.format(self.key)
