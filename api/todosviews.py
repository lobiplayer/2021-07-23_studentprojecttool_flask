from flask import Blueprint, jsonify, request
from . import db
from .models import Todo
from .models import Deadline
import datetime
import random