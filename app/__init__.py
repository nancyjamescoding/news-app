from flask import Flask
from .config import Config, devConfig

#Initializing application
app = Flask (__name__)

#setting up the application
app.config.from_object(devConfig)

from app import views