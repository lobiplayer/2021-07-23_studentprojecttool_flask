from flask import Blueprint, jsonify, request
from . import db
from .usersmodels import User
import datetime
import random

users = Blueprint('usersmodel', __name__)


@users.route('/add_user', methods=['POST'])
def add_user():

    user_data = request.get_json()

    new_user = User(name=user_data['name'], email=user_data['email'], password=user_data['password'],
                    date_of_birth=user_data['date_of_birth'],  created_at=user_data['created_at'],  updated_at=user_data['updated_at'])

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
