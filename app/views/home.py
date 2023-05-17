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
@app.route("/home/")
def home():

    df_pubs = Functions().get_s3_pubs()
    df_pubs.to_csv(os.getcwd() + '/files/venues.csv', index=False, sep=',', encoding='utf-8')

    df_reviews = Functions().get_s3_reviews()
    df_reviews.to_csv(os.getcwd() + '/files/scores.csv', index=False, sep=',', encoding='utf-8')

    df_areas = Functions().get_s3_areas()
    df_areas.to_csv(os.getcwd() + '/files/areas.csv', index=False, sep=',', encoding='utf-8')

    df_crawls = Functions().get_s3_crawls()
    df_crawls.to_csv(os.getcwd() + '/files/crawls.csv', index=False, sep=',', encoding='utf-8')

    df_stations = Functions().get_s3_stations()
    df_stations.to_csv(os.getcwd() + '/files/stations.csv', index=False, sep=',', encoding='utf-8')

    df_photos = Functions().get_s3_photos()
    df_photos.to_csv(os.getcwd() + '/files/photos.csv', index=False, sep=',', encoding='utf-8')

    df_all_area = df_pubs[['name', 'area_identity']]
    print(df_all_area)
    df_all_area_group = df_all_area.groupby(['area_identity'], as_index=False).count()
    print(df_all_area_group)
    df_all_area_count = pd.merge(df_all_area_group, df_areas, how='left', on='area_identity') \
        .rename(columns={'name': 'count'}).astype(str) \
        .sort_values(by=['count'], ascending=False)
    areas_json = Functions().df_to_dict(df_all_area_count)
    # print(df_all_area_count)
    # pubs_reviews_json = Functions().df_to_dict(
    #     Functions().get_pubs_reviews().sort_values(by=['score'], ascending=False))
    # df_crawl = Functions().get_crawls()

    df_crawl_last = df_crawls.tail(1)
    start = df_crawl_last['start'].values[0]
    walk = df_crawl_last['walk'].apply(str).values[0]
    favourite = df_crawl_last['favourite'].values[0]
    stops = df_crawl_last['stops'].apply(str).values[0]
    criteria = df_crawl_last['criteria'].values[0]
    # df_pubs = Functions().get_pubs_reviews()
    df_pub = df_pubs.loc[df_pubs['place'] == start]
    pubs_json = Functions().df_to_dict(df_pubs)
    pub_json = Functions().df_to_dict(df_pub)
    return render_template('home.html', pubs_reviews=pubs_json, photo_array=config, map_view="stations",
                               map_lat=51.5, map_lng=-0.1, config=config, google_key=config2['google_key'],
                               row_loop=range(3), col_loop=range(4), areas=areas_json, start=start,
                                   walk=walk, favourite=favourite, stops=stops, criteria=criteria,
                           pubs=pubs_json, pub=pub_json, config2=config2)
