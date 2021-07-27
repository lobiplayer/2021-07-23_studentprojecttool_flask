from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask('GARDONE', root_path=web_dir)

web_dir = os.path.join(os.path.dirname(
    os.path.abspath(file)), 'api')
