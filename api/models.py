from . import db

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    todo_text = db.Column(db.String(50), nullable=False)
    is_done = db.Column(db.Boolean)
    deadline_id = db.Column(db.Integer)
    user_id = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)

class Deadline(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(50), nullable=False)
    date = db.Column(db.DateTime)
    subject = db.Column(db.String)
    user_id = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime)
    updated_at = db.Column(db.DateTime)