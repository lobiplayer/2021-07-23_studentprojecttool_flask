from . import db
class Deadline(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(50), nullable=False)
    date = db.Column(db.String(50), nullable=False)
    subject = db.Column(db.String)
    user_id = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

    