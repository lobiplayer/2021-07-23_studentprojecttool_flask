from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from views import main
from rewardsviews import rewards
from usersviews import users

load_dotenv()

db = SQLAlchemy()



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

db.init_app(app)

migrate = Migrate(app, db)

app.register_blueprint(main)

app.register_blueprint(rewards)

app.register_blueprint(users)

app.run()