from flask import Flask
from flask_sqlalchemy import SQLAlchemy


import os

app = Flask(__name__ , static_folder='static')

from app.main.routes import bp as main_blueprint
app.register_blueprint(main_blueprint)
