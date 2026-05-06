from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

# create the ORM instance and name it db
db = SQLAlchemy()

# create a function named create_app and initialize the flask app
def create_app():
    app = Flask(__name__)
    # load the configurations from the config.py file 
    app.config.from_object(Config)
    
    # link the ORM instance created to the app 
    db.init_app(app)
    
    return app
    