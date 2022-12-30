from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Recom(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    data=db.Column(db.String(50))
    date=db.Column(db.DateTime(timezone=True),default=func.now())
    user_email=db.Column(db.String(100),db.ForeignKey('user.email'))

class User(db.Model,UserMixin):
    id=db.Column(db.Integer,primary_key=True)
    email=db.Column(db.String(100),unique=True)
    password=db.Column(db.String(100))
    recomm=db.relationship('Recom')