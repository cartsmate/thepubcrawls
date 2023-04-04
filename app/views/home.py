import os
import json
from configparser import ConfigParser
from flask import render_template, redirect, url_for
from app import app
from config import Configurations
from functions.functions import Functions

config = Configurations().get_config()
functions = Functions()


@app.route("/home/<on_line>")
def home(on_line):
    print(f'/home/{on_line}')
    if on_line == 'true':
        print('on-line')
        functions.get_pubs().to_csv(os.getcwd() + '/files/venues.csv', sep=',', encoding='utf-8', index=False)
        functions.get_reviews().to_csv(os.getcwd() + '/files/reviews.csv', sep=',', encoding='utf-8', index=False)
        functions.get_areas().to_csv(os.getcwd() + '/files/areas.csv', sep=',', encoding='utf-8', index=False)
        functions.get_stations().to_csv(os.getcwd() + '/files/stations.csv', sep=',', encoding='utf-8', index=False)
    photo_array = json.loads(config['column_photo'])
    return render_template('home.html', photo_array=photo_array, map_view="stations", map_lat=51.5, map_lng=-0.1,
                           row_loop=range(3), col_loop=range(4))
