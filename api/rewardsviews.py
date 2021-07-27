from flask import Blueprint, jsonify, request
from rewardsmodel import RewardsList
import datetime
import random
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
rewards = Blueprint('rewards', __name__)


@rewards.route('/add_rewardslist', methods=['POST'])
def add_rewardslist():

    rewards_data = request.get_json()
    print(rewards_data)

    latest_state = RewardsList.query.filter_by(user_id = rewards_data['user_id']).order_by(RewardsList.id.desc()).first()
    
    set_state = ""
    
    if latest_state:
        if latest_state.state == "Seedling":
            set_state = "Germination"
        
        elif latest_state.state == "Germination":
            set_state = "Shoots"
        
        elif latest_state.state == "Shoots":
            set_state = "Budding"

        elif latest_state.state == "Budding":
            set_state = "Blooming"

        else: 
            set_state = "Seedling"

    else:
        set_state = "Seedling"
    

    new_rewards = RewardsList(points=rewards_data['points'], user_id = rewards_data['user_id'], 
    task_completed = rewards_data['task_completed'], state = set_state)

#saving it to the database:
    db.session.add(new_rewards)
    db.session.commit()

    return 'Done', 201



@rewards.route('/rewardslist', methods=['POST'])
def rewardslist():

    rewards_data = request.get_json()
    print('rewards')
    print(rewards_data)
# geting the Todo records from the database. here we have to make where todo.user_id == currentuser
    rewards_list = RewardsList.query.filter_by(user_id = rewards_data['user_id'])
    #this is the list that will be send to the react app:
    rewardslist = [[{'points':0 ,'user_id': rewards_data['user_id'], 'task_completed': 'Welcome! Start your garden today!', 'state': "Packet"}]]

#every todo from the database will be formatted in a dictionary, this will be appended to the todos list (2 lines back)
    for data in rewards_list:
        rewardslist.append([{'points':data.points ,'user_id': data.user_id, 'task_completed': data.task_completed, 'state': data.state}])

    print(rewardslist)
#this will be send to the client (this will be the response for the get request)
    return jsonify({'rewardslist' : rewardslist})


@rewards.route('/rewardslist_totalpoints', methods=['POST'])
def rewardslist_totalpoints():

    rewards_data = request.get_json()

# geting the Todo records from the database. here we have to make where todo.user_id == currentuser
    rewards_list = RewardsList.query.filter_by(user_id = rewards_data['user_id'])
    #this is the list that will be send to the react app:
    total_points = 0
    for value in rewards_list:
        total_points += value.points

#every todo from the database will be formatted in a dictionary, this will be appended to the todos list (2 lines back)
    print(total_points)

#this will be send to the client (this will be the response for the get request)
    return jsonify({'total_points' : total_points})


