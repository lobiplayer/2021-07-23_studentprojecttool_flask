from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from .views import main
from .rewardsviews import rewards
from .usersviews import users
import re

load_dotenv()

db = SQLAlchemy()



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = re.sub('postgres', 'postgresql', os.environ.get('DATABASE_URL'))

db.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(main)

app.register_blueprint(rewards)

app.register_blueprint(users)