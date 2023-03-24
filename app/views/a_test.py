import os
import json
from configparser import ConfigParser
from flask import render_template
from app import app
from config import Configurations

config = Configurations().get_config()


@app.route("/")
@app.route("/test")
def test():
    print('/test')
    return render_template('a_test.html', google_key=config['google_key'])
