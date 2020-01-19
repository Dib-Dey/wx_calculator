from flask import Flask
from config import Config

flask_obj = Flask(__name__)
#following method of flask can help applying the dictionary items in config file
flask_obj.config.from_object(Config)

from app import routes