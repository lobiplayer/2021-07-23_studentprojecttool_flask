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
    new_rewards = RewardsList()

# [{ image: require('../assets/Seedling.png'), message: "You have just planted a new seed. Complete another task and watch your plant grow." }],
#         [{ image: require('../assets/Germination.png'), message: "Your plant is growing well. Keep going!" }],
#         [{ image: require('../assets/Shoots.png'), message: "Look at those green leaves." }],
#         [{ image: require('../assets/Budding.png'), message: "One more task and your flower will bloom!" }],
#         [{ image: require('../assets/Blooming.png'), message: "Congratulations! You have harvested a new flower. When you're ready, complete another task to plant a new seed!" }],


#saving it to the database:
    db.session.add(new_rewards)
    db.session.commit()

    return 'Done', 201



@rewards.route('/rewardslist', methods=['GET'])
def rewardslist():

    # new_rewards = RewardsList(points="100", user_id = '1', task_completed = 'Day Five', state = "Blooming")
    # db.session.add(new_rewards)
    # db.session.commit()


# geting the Todo records from the database. here we have to make where todo.user_id == currentuser
    rewards_list = RewardsList.query.all()
    #this is the list that will be send to the react app:
    rewardslist = []

#every todo from the database will be formatted in a dictionary, this will be appended to the todos list (2 lines back)
    for data in rewards_list:
        rewardslist.append([{'points':data.points ,'user_id': data.user_id, 'task_completed': data.task_completed, 'state': data.state}])

#this will be send to the client (this will be the response for the get request)
    return jsonify({'rewardslist' : rewardslist})


# @rewards.route('/add_rewardsoutput', methods=['POST'])
# def add_rewardsoutput():

#     new_output = Rewardsoutput(image_url='Seedling', message = 'You have just planted a new seed. Complete another task and watch your plant grow.')


# # [{ image: require('../assets/Seedling.png'), message: "You have just planted a new seed. Complete another task and watch your plant grow." }],
# #         [{ image: require('../assets/Germination.png'), message: "Your plant is growing well. Keep going!" }],
# #         [{ image: require('../assets/Shoots.png'), message: "Look at those green leaves." }],
# #         [{ image: require('../assets/Budding.png'), message: "One more task and your flower will bloom!" }],
# #         [{ image: require('../assets/Blooming.png'), message: "Congratulations! You have harvested a new flower. When you're ready, complete another task to plant a new seed!" }],


# #saving it to the database:
#     db.session.add(new_todo)
#     db.session.commit()

#     return 'Done', 201



# @rewards.route('/rewardsoutput', methods=['GET'])
# def rewardsoutput():


# # geting the Todo records from the database. here we have to make where todo.user_id == currentuser
#     rewardsoutput_list = Rewardsoutput.query.all()
#     #this is the list that will be send to the react app:
#     rewardsoutput = []

# #every todo from the database will be formatted in a dictionary, this will be appended to the todos list (2 lines back)
#     for data in rewardsoutput_list:
#         rewardsoutput.append({'image':data.image_url ,'message': data.message})

# #this will be send to the client (this will be the response for the get request)
#     return jsonify({'rewardsoutput' : rewardsoutput})




