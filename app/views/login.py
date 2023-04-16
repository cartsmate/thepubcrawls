import os
import json
from configparser import ConfigParser
from flask import render_template, redirect, url_for, session, request, g
from app import *
from config import Configurations
from functions.functions import Functions

config = Configurations().get_config()
functions = Functions()


# @app.before_request
# def before_request():
#     g.user = None
#     if 'user_id' in session:
#         user = [x for x in users if x.id == session['user_id']][0]
#         g.user = user

@app.route("/login", methods=['GET', 'POST'])
def login():
    print("login")
    if request.method == 'POST':
        print("login: POST")
        # session.pop('user_id', None)
        username = request.form['username']
        password = request.form['password']
        # user = [x for x in users if x.username == username][0]
        # if user and user.password == password:
        if True == True:
            print("login: POST - true")
            session['user_id'] = username
            session['logged_in'] = True
            print('true = true')
            _get = session.get('logged_in')
            print(_get)
            return redirect(url_for('index'))
        print("login: POST - false")
        return redirect(url_for('login'))
    print("login: GET")
    return render_template('login.html')
