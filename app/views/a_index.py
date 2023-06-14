import os
import json
from configparser import ConfigParser
from flask import render_template, redirect, url_for, session, g
from app import app
from config import Configurations

config = Configurations().get_config()
functions = Functions()


@app.route("/a_index")
def a_index():
    return render_template('a_index.html')
