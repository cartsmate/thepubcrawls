import os
import json
from configparser import ConfigParser
from flask import render_template
from app import app
from config import Configurations

config = Configurations().get_config()


@app.route("/")
@app.route("/test")
def pub_test(x, y):
    print('/test')
    return x + y
    # return render_template('a_test.html', google_key=config['google_key'])
