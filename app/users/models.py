
from app import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250))
    email = db.Column(db.String(120), index=True, unique=True)
    password = db.Column(db.String(128), nulltable=True)
