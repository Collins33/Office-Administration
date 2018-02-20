#third party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

#LOCAL IMPORT
from config import app_config


#initialize the db
db=SQLAlchemy()

#inittilize the loginManager object
login_manager=LoginManager()


def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_message="YOU MUST BE LOGGED IN"
    login_manager.login_view="auth.login"

    return app
    
