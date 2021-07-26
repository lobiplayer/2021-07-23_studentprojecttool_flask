from flask import Blueprint, jsonify, request
from . import db
from .usersmodels import User
import datetime
import random

users = Blueprint('users', __name__)


@users.route('/add_user', methods=['POST'])
def add_user():

    # user_data = request.get_json()

    # token = ''.join(random.choice(characters) for i in range(15))

    # new_user = User(name=user_data['name'], email=user_data['email'], password=user_data['password'], 
    #                 date_of_birth=user_data['date_of_birth'],   created_at = datetime.datetime.now(),  updated_at= None)


    new_user = User(name='Testing', email='testing@gmail.com', password='Testing123$$$',
                    date_of_birth='01-01-2020')

    db.session.add(new_user)
    db.session.commit()


    return 'User Created', 201


@users.route('/users')
def user():

    user_list = User.query.all()
    users = []

    for user in user_list:
        users.append({'name': user.name, 'email': user.email,
                      'password': user.password, 'date_of_birth': user.date_of_birth})

    return jsonify({'users': users})


@users.route('/user_login', methods=['POST'])
def user_login():

    login_data = request.get_json()
    print(login_data)

    check_email = User.query.filter_by(email = login_data['email']).first()

    user_id = ""

    if (check_email):
        if check_email.password == login_data['password']:
            user_id = check_email.id
            print(user_id)
            return jsonify({'user_id': user_id})
        
        else:
            print(user_id)
            return jsonify({'user_id': user_id})
    
    else:
        print(user_id)
        return jsonify({'user_id': user_id})


