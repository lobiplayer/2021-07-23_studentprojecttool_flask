from . import db


class Rewardsoutput(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    image_url = db.Column(db.Text)
    message = db.Column(db.Text)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

class RewardsList(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    points = db.Column(db.Integer, nullable = False)
    user_id = db.Column(db.Integer, nullable=False)
    task_completed = db.Column(db.String)
    state = db.Column(db.String)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)