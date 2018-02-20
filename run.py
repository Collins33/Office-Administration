import os

from app import create_app

#get the flask configuratuion from the os
config_name=os.getenv('FLASK_CONFIG')

#create app by passing the configuration name to create_app
app=create_app(config_name)

if __name__ == '__main__':
    app.run()