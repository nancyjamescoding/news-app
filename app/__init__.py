from flask import Flask
from config import devConfig

#Initializing application
app = Flask(__name__,instance_relative_config = True)

#setting up the application
app.config.from_object(devConfig)
# app.config.from_pyfile('config.py')

from app import views