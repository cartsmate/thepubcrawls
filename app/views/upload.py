import os
import json
import pandas as pd
from configparser import ConfigParser
from flask import render_template, redirect, url_for, g, session
from app import app
from config import Configurations
from functions.functions import Functions

config = Configurations().get_config()
config2 = Configurations().get_config2()


# @app.route("/home/<on_line>")
# def home(on_line):
    # if session.get('logged_in') != True:
    #     return redirect(url_for('login'))
    # if on_line == 'true':
    #     Functions().get_s3_pubs().to_csv(os.getcwd() + '/files/' + config['pub']['aws_key'], sep=',', encoding='utf-8', index=False)
    #     Functions().get_s3_reviews().to_csv(os.getcwd() + '/files/' + config['review']['aws_key'], sep=',', encoding='utf-8', index=False)
    #     Functions().get_s3_areas().to_csv(os.getcwd() + '/files/' + config['area']['aws_key'], sep=',', encoding='utf-8', index=False)
    #     Functions().get_s3_stations().to_csv(os.getcwd() + '/files/' + config['station']['aws_key'], sep=',', encoding='utf-8', index=False)
@app.route("/upload/")
def upload():

    return render_template('upload.html')
