import os
import json
import pandas as pd
from configparser import ConfigParser
from flask import render_template, redirect, url_for, g, session
from app import app
from config import Configurations
from functions.functions import Functions

config = Configurations().get_config()


# @app.route("/home/<on_line>")
# def home(on_line):
    # if session.get('logged_in') != True:
    #     return redirect(url_for('login'))
    # if on_line == 'true':
    #     Functions().get_s3_pubs().to_csv(os.getcwd() + '/files/' + config['pub']['aws_key'], sep=',', encoding='utf-8', index=False)
    #     Functions().get_s3_reviews().to_csv(os.getcwd() + '/files/' + config['review']['aws_key'], sep=',', encoding='utf-8', index=False)
    #     Functions().get_s3_areas().to_csv(os.getcwd() + '/files/' + config['area']['aws_key'], sep=',', encoding='utf-8', index=False)
    #     Functions().get_s3_stations().to_csv(os.getcwd() + '/files/' + config['station']['aws_key'], sep=',', encoding='utf-8', index=False)
@app.route("/home/")
def home():
    df_all = Functions().get_pubs_reviews()
    df_areas = Functions().get_areas()
    df_all_area = df_all[['name', 'area_identity']]
    df_all_area_group = df_all_area.groupby(['area_identity'], as_index=False).count()
    df_all_area_count = pd.merge(df_all_area_group, df_areas, how='left', on='area_identity') \
        .rename(columns={'name': 'count'}).astype(str) \
        .sort_values(by=['count'], ascending=False)
    # print(df_all_area_count)
    areas_json = Functions().df_to_dict(df_all_area_count)
    pubs_reviews_json = Functions().df_to_dict(
        Functions().get_pubs_reviews().sort_values(by=['score'], ascending=False))

    return render_template('home.html', pubs_reviews=pubs_reviews_json, photo_array=config, map_view="stations", map_lat=51.5, map_lng=-0.1, config=config,
                           row_loop=range(3), col_loop=range(4), areas=areas_json)
