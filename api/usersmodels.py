from .rewardsmodel import RewardsList
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    date_of_birth = db.Column(db.String(50))
    rewards = db.relationship('RewardsList', backref = 'user')
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)
