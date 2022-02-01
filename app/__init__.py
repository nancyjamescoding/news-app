from distutils import extension
from ensurepip import bootstrap
from flask import Flask
from config import devConfig
from flask_bootstrap import Bootstrap

#Initializing application
app = Flask(__name__,instance_relative_config = True)

#setting up the application
app.config.from_object(devConfig)

# app.config.from_pyfile('config.py')

#initializing  flask extensions
bootstrap = Bootstrap(app)

from app import views