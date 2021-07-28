from flask import Blueprint, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from .models import Todo
from .models import Deadline
import datetime
import random
from datetime import date
db = SQLAlchemy()
main = Blueprint('main', __name__)

@main.route('/add_todo', methods=['POST'])
def add_todo():

    #getting the information from the POST request in json format:
    todo_data = request.get_json()
# adding a new record for the database. deadline_id and user_id are set as random number for now:
    new_todo = Todo(todo_text=todo_data['todo_text'], is_done=False, deadline_id=random.randint(1, 1000000), user_id=todo_data["user_id"], created_at = datetime.datetime.now(), updated_at= None)

#saving it to the database:
    db.session.add(new_todo)
    db.session.commit()

    return 'Done', 201

@main.route('/todos', methods=['POST'])
def todos():

    user_id = request.get_json()

# geting the Todo records from the database. here we have to make where todo.user_id == currentuser
    todo_list = Todo.query.filter_by(user_id=user_id['user_id'])
    #this is the list that will be send to the react app:
    todos = []

#every todo from the database will be formatted in a dictionary, this will be appended to the todos list (2 lines back)
    for todo in todo_list:
        todos.append({'id':todo.id ,'todo_text': todo.todo_text, 'is_done': todo.is_done, 'deadline_id': todo.deadline_id, 'user_id': user_id['user_id'], 'created_at': todo.created_at, 'updated_at': todo.updated_at})

#this will be send to the client (this will be the response for the get request)
    return jsonify({'todos' : todos})


@main.route('/add_deadline', methods=['POST'])
def add_deadline():

    deadline_data = request.get_json()

    new_deadline = Deadline(description=deadline_data['description'], date=deadline_data['date'], subject=deadline_data['subject'], user_id=deadline_data['user_id'], created_at = datetime.datetime.now(), updated_at= None)

    db.session.add(new_deadline)
    db.session.commit()

    return 'Done', 201

@main.route('/deadlines', methods=['POST'])
def deadlines():

    user_data = request.get_json()
# geting the Todo records from the database. here we have to make where todo.user_id == currentuser
    deadline_list = Deadline.query.filter_by(user_id = user_data['user_id'])
    deadlines = []
    #this is the list that will be send to the react app:
    for deadline in deadline_list:
        deadlines.append({'id':deadline.id ,'description': deadline.description, 'deadline_date': deadline.date, 'subject': deadline.subject, 'user_id': deadline.user_id, 'created_at': deadline.created_at, 'updated_at': deadline.updated_at})

    return jsonify({'deadlines' : deadlines})



@main.route('/todolist_homepage', methods=['POST'])
def todolist_homepage():

    user_id = request.get_json()
    print('homepage')
    print(user_id)
# geting the Todo records from the database. here we have to make where todo.user_id == currentuser
    oldest_todo = Todo.query.filter_by(user_id = user_id['user_id']).limit(5)
    #this is the list that will be send to the react app:
    todolist_homepage = [{'todo_text':'Tackle a task today!' ,'deadline_id': user_id['date_today']}]
    print(oldest_todo)

#every todo from the database will be formatted in a dictionary, this will be appended to the todos list (2 lines back)
    for data in oldest_todo:
        todolist_homepage.append({'todo_text':data.todo_text ,'deadline_id': data.deadline_id})

    print(todolist_homepage)
#this will be send to the client (this will be the response for the get request)
    return jsonify({'todolist_homepage' : todolist_homepage})



@main.route('/deadline_homepage', methods=['POST'])
def deadline_homepage():

    user_id = request.get_json()
    print('deadline')
    print(user_id)
# geting the Todo records from the database. here we have to make where todo.user_id == currentuser
    deadline = Deadline.query.filter_by(user_id = user_id['user_id']).limit(5)
    #this is the list that will be send to the react app:
    deadline_homepage = [{'date': user_id['date_today'],'subject': 'Congratulations', 'description': 'for showing up and getting the work done!'}]
    print(deadline_homepage)

#every todo from the database will be formatted in a dictionary, this will be appended to the todos list (2 lines back)
    for data in deadline:
        deadline_homepage.append({'date':data.date ,'subject': data.subject, 'description': data.description})

    print(deadline_homepage)
#this will be send to the client (this will be the response for the get request)
    return jsonify({'deadline_homepage' : deadline_homepage})

@main.route('/test', methods=['GET'])
def test():


# geting the Todo records from the database. here we have to make where todo.user_id == currentuser
    todo_list = Todo.query.all()
    #this is the list that will be send to the react app:
    todos = []

#every todo from the database will be formatted in a dictionary, this will be appended to the todos list (2 lines back)
    for todo in todo_list:
        todos.append({'id':todo.id ,'todo_text': todo.todo_text, 'is_done': todo.is_done, 'deadline_id': todo.deadline_id, 'user_id': todo.id, 'created_at': todo.created_at, 'updated_at': todo.updated_at})

#this will be send to the client (this will be the response for the get request)
    return jsonify({'todos' : todos})
