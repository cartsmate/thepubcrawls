import os
import json
from configparser import ConfigParser
from flask import render_template, redirect, url_for
from app import app
from config import Configurations
from functions.functions import Functions

config = Configurations().get_config()
functions = Functions()


@app.route("/")
@app.route("/index")
def index():
    print('/index')

    # return redirect(url_for('home'))
    return render_template('index.html')
