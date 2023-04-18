import os
import json
from configparser import ConfigParser
from flask import render_template, redirect, url_for, session, g
from app import app
from config import Configurations
from functions.functions import Functions

config = Configurations().get_config()
functions = Functions()


@app.route("/")
def route():
    # return render_template('login.html')
    return redirect(url_for('home'))


@app.route("/index")
def index():
    # _get = session.get('logged_in')
    # print(_get)
    # if session.get('logged_in') != True:
    #     return redirect(url_for('login'))
    return redirect(url_for('home'))
    # return render_template('index.html')
