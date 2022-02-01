from distutils import extension
from ensurepip import bootstrap
from flask import Flask
from config import devConfig
from flask_bootstrap import Bootstrap
from config import config_options


# #Initializing application
# app = Flask(__name__,instance_relative_config = True)

# #setting up the application
# app.config.from_object(devConfig)

# # app.config.from_pyfile('config.py')

#initializing  flask extensions
bootstrap = Bootstrap()
def create_app(config_name):
    app = Flask(__name__)
    ## Creating the app configurations
    app.config.from_object(config_options[config_name])

    # Initializing flask extensions
    bootstrap.init_app(app)

    # Will add the views and forms
    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    return app
