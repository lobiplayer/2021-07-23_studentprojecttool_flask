from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

load_dotenv()

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

    db.init_app(app)

    migrate = Migrate(app, db)

    from .views import main
    app.register_blueprint(main)

    from .rewardsviews import rewards
    app.register_blueprint(rewards)

    from .usersviews import users
    app.register_blueprint(users)

    return app