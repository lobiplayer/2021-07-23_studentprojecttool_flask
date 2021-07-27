from flask import Blueprint, jsonify, request
from . import db
from .models import Deadline
import datetime

deadlines = Blueprint('deadlines', __name__)

@deadlines.route('/add_deadline', methods=['POST'])
def add_deadline():

    deadline_data = request.get_json()

    new_deadline = Deadline(description=deadline_data['description'], date=deadline_data['date'], subject=deadline_data['subject'], user_id=deadline_data['user_id'], created_at = datetime.datetime.now(), updated_at= None)

    db.session.add(new_deadline)
    db.session.commit()

    return 'Done', 201

@deadlines.route('/deadlines', methods=['POST'])
def deadlines():

    user_data = request.get_json()
# geting the Todo records from the database. here we have to make where todo.user_id == currentuser
    deadline_list = Deadline.query.filter_by(user_id = user_data['user_id'])
    deadlines = []
    #this is the list that will be send to the react app:
    for deadline in deadline_list:
        deadlines.append({'id':deadline.id ,'description': deadline.description, 'deadline_date': deadline.date, 'subject': deadline.subject, 'user_id': deadline.user_id, 'created_at': deadline.created_at, 'updated_at': deadline.updated_at})

    return jsonify({'deadlines' : deadlines})