from flask import Flask
from flask_sqlalchemy import SQLAlchemy


import os

app = Flask(__name__ , static_folder='static')

from app.main.routes import bp as main_blueprint
from app.prediction.routes import bp as predict_blueprint

app.register_blueprint(main_blueprint)
app.register_blueprint(predict_blueprint)
