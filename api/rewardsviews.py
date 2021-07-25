from flask import Blueprint, jsonify, request
from . import db
from .rewardsmodel import Rewardsoutput
from .rewardsmodel import RewardsList
import datetime
import random


rewards = Blueprint('rewards', __name__)


@rewards.route('/add_rewardslist', methods=['POST'])
def add_rewardslist():

    rewards_data = request.get_json()
    print(rewards_data)
    new_rewards = RewardsList(points=rewards_data.points, user_id = rewards_data.user_id, task_completed = rewards_data.task_completed, state = "Blooming")

#saving it to the database:
    db.session.add(new_rewards)
    db.session.commit()

    return 'Done', 201



@rewards.route('/rewardslist', methods=['GET'])
def rewardslist():


# geting the Todo records from the database. here we have to make where todo.user_id == currentuser
    rewards_list = RewardsList.query.all()
    #this is the list that will be send to the react app:
    rewardslist = []

#every todo from the database will be formatted in a dictionary, this will be appended to the todos list (2 lines back)
    for data in rewards_list:
        rewardslist.append([{'points':data.points ,'user_id': data.user_id, 'task_completed': data.task_completed, 'state': data.state}])

#this will be send to the client (this will be the response for the get request)
    return jsonify({'rewardslist' : rewardslist})

