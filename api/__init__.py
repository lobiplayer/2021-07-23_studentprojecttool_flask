from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

load_dotenv()

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

    db.init_app(app)

    migrate = Migrate(app, db)

    from .deadlinesviews import deadlines
    app.register_blueprint(deadlines)

    from .todosviews import todos
    app.register_blueprint(todos)

    from .rewardsviews import rewards
    app.register_blueprint(rewards)

    from .usersviews import users
    app.register_blueprint(users)

    return app