from flask import Flask
from flask_sqlalchemy import SQLAlchemy


import os

app = Flask(__name__)
# SECRET_KEY = os.urandom(32)
# app.config['SECRET_KEY'] = SECRET_KEY
# app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///library.db'


# db = SQLAlchemy(app)
# db.create_all()


from app.main.routes import bp as main_blueprint
app.register_blueprint(main_blueprint)