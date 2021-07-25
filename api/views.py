from flask import Blueprint, jsonify, request
from . import db
from .models import Todo
from .models import Deadline
import datetime
import random

main = Blueprint('main', __name__)

@main.route('/add_todo', methods=['POST'])
def add_todo():

    #getting the information from the POST request in json format:
    todo_data = request.get_json()
# adding a new record for the database. deadline_id and user_id are set as random number for now:
    new_todo = Todo(todo_text=todo_data['todo_text'], is_done=False, deadline_id=random.randint(1, 1000000), user_id=random.randint(1, 1000000), created_at = datetime.datetime.now(), updated_at= None)

#saving it to the database:
    db.session.add(new_todo)
    db.session.commit()

    return 'Done', 201

@main.route('/todos', methods=['GET'])
def todos():

# geting the Todo records from the database. here we have to make where todo.user_id == currentuser
    todo_list = Todo.query.all()
    #this is the list that will be send to the react app:
    todos = []

#every todo from the database will be formatted in a dictionary, this will be appended to the todos list (2 lines back)
    for todo in todo_list:
        todos.append({'id':todo.id ,'todo_text': todo.todo_text, 'is_done': todo.is_done, 'deadline_id': todo.deadline_id, 'user_id': todo.user_id, 'created_at': todo.created_at, 'updated_at': todo.updated_at})

#this will be send to the client (this will be the response for the get request)
    return jsonify({'todos' : todos})


@main.route('/add_deadline', methods=['POST'])
def add_deadline():

    deadline_data = request.get_json()

    new_deadline = Deadline(description=deadline_data['description'], date=datetime.datetime(deadline_data['date']), subject=deadline_data['subject'], user_id=random.randint(1, 1000000), created_at = datetime.datetime.now(), updated_at= None)

    db.session.add(new_deadline)
    db.session.commit()

    return 'Done', 201

@main.route('/deadlines', methods=['GET'])
def deadlines():
    deadline_list = Deadline.query.all()
    deadlines = []

    for deadline in deadline_list:
        deadlines.append({'id':deadline.id ,'description': deadline.description, 'date': deadline.date, 'subject': deadline.subject, 'user_id': deadline.user_id, 'created_at': deadline.created_at, 'updated_at': deadline.updated_at})

    return jsonify({'deadlines' : deadlines})