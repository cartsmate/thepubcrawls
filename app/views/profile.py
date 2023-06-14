import os
import json
from configparser import ConfigParser
from flask import render_template, redirect, url_for, session, g
from app import app
from config import Configurations

config = Configurations().get_config()


@app.route("/profile")
def profile():
    # if not g.user:
    #     print('/profile')
    #     return redirect(url_for('login'))
    return render_template('profile.html')
