"""
Author(s): 
Date: 
Release: 
Description: 
"""

#time import
import time

#Imports Flask Libraries
from re import template
from flask import Flask, render_template, request, session, jsonify, redirect, url_for

#Imports Requests Library
import requests

#Imports OS Library
import os

#Imports JSON Library
import json

#Imports Config Objects from Configuration File
from .config import DevelopmentConfig, ProductionConfig

#Import Utils
from .utils import *

#Import Classes
from BUGTRACKER.model.account import *
from BUGTRACKER.model.project import *
from BUGTRACKER.model.bug import *

"""
"""
def create_app():
    #Declares Flask Application
    app = Flask(__name__, instance_relative_config=True)

    #Detects Flask Environment and Sets Proper Configuration   
    print("----- Setting Configuration -----")
    if app.config.get("ENV") == "development":
        app.config.from_object(DevelopmentConfig)
    elif app.config.get("ENV") == "production":
        app.config.from_object(ProductionConfig)
    print(" * Configuration:", app.config)
    print("----- Configuration Set -----")

    #Ensures Instance Folder Exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass



    #Route for Home
    @app.route("/", methods=['GET', 'POST'])
    def index():
        return render_template('index.html')

    #route for time test
    @app.route('/time')
    def get_current_time():
        return {'time': time.time()}
    

    

    return app