import os
import json
import random
import pandas as pd
from configparser import ConfigParser
from flask import render_template, redirect, url_for, g, session
from app import app
from config import Configurations
from functions.functions import Functions
from app.static.pythonscripts.dataframes import Dataframes

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
    if config2['env'] == 'prod':
        obj_df = Functions().s3_read('counter_prod', ['pub_counter'])
    else:
        obj_df = pd.read_csv(os.getcwd() + '/files/counter_qual.csv')

    print(obj_df)
    obj_df["pub_counter"] = obj_df["pub_counter"] + 1

    print(obj_df)

    if config2['env'] == 'prod':
        s3_resp = Functions().s3_write(obj_df, 'counter_prod.csv')
    else:
        obj_df.to_csv(os.getcwd() + '/files/counter_qual.csv', sep=',', encoding='utf-8', index=False)

    counter = obj_df["pub_counter"].values[0].astype(str).zfill(6)
    print(counter)
    # df_pubs = Functions().get_s3_pubs()
    # df_pubs.to_csv(os.getcwd() + '/files/venues.csv', index=False, sep=',', encoding='utf-8')
    # print(df_pubs)
    #
    # df_reviews = Functions().get_s3_reviews()
    # df_reviews.to_csv(os.getcwd() + '/files/scores.csv', index=False, sep=',', encoding='utf-8')
    #
    # df_areas = Functions().get_s3_areas()
    # df_areas.to_csv(os.getcwd() + '/files/areas.csv', index=False, sep=',', encoding='utf-8')
    #
    # df_crawls = Functions().get_s3_crawls()
    # df_crawls.to_csv(os.getcwd() + '/files/crawls.csv', index=False, sep=',', encoding='utf-8')
    #
    # df_stations = Functions().get_s3_stations()
    # df_stations.to_csv(os.getcwd() + '/files/stations.csv', index=False, sep=',', encoding='utf-8')
    #
    # df_photos = Functions().get_s3_photos()
    # df_photos.to_csv(os.getcwd() + '/files/photos.csv', index=False, sep=',', encoding='utf-8')
    # else:
    df_pubs = Functions().get_pubs()
    df_areas = Functions().get_areas()
    df_crawls = Functions().get_crawls()
    df_photos = Functions().get_photos()

    df_all_area = df_pubs[['name', 'area_identity']]
    # print(df_all_area)
    df_all_area_group = df_all_area.groupby(['area_identity'], as_index=False).count()
    # print(df_all_area_group)
    df_all_area_count = pd.merge(df_all_area_group, df_areas, how='left', on='area_identity') \
        .rename(columns={'name': 'count'}).astype(str) \
        .sort_values(by=['count'], ascending=False)
    areas_json = Functions().df_to_dict(df_all_area_count)

    df_all_area_group2 = df_all_area.groupby(['area_identity'], as_index=False).count()
    # print(df_all_area_group2)
    df_all_area_count2 = pd.merge(df_all_area_group2, df_areas, how='left', on='area_identity')\
        .sort_values(by=['area'], ascending=True)
    # print(df_all_area_count2)
    areas_json2 = Functions().df_to_dict(df_all_area_count2)

    df_crawl_last = df_crawls.tail(1)
    # print(df_crawl_last)
    start = df_crawl_last['start'].values[0]
    # print(start)
    walk = df_crawl_last['walk'].apply(str).values[0]
    favourite = df_crawl_last['favourite'].values[0]
    stops = df_crawl_last['stops'].apply(str).values[0]
    criteria = df_crawl_last['criteria'].values[0]
    # df_pubs = Functions().get_pubs_reviews()
    df_pub = df_pubs.loc[df_pubs['place'] == start]
    df_pub['colour'] = '#d9534f'
    # print(df_pub)
    pub_json = Functions().df_to_dict(df_pub)

    df_pubs['colour'] = '#0275d8'
    pubs_json = Functions().df_to_dict(df_pubs)
    pubs_total = df_pubs.shape[0]
    # print('total: ' + str(pubs_total))
    random_identity = random.randint(0, pubs_total)
    # print('random: ' + str(pubs_random))
    pub_random = df_pubs.iloc[[random_identity]]
    df = pd.merge(pub_random, df_photos, how='left', on='pub_identity')
    photo_id = df['photo_identity'].values[0]
    # print(photo_id)
    # create random number
    # find index from random number in df_pubs
    # return single pub as random

    list_L = df_pubs[['latitude', 'longitude']].values.tolist()
    _lat = []
    _long = []
    for l in list_L:
        _lat.append(l[0])
        _long.append(l[1])

    review_lat = sum(_lat) / len(_lat)
    review_long = sum(_long) / len(_long)

    return render_template('home.html', pubs_reviews=pubs_json, photo_array=config, map_view="stations",
                            map_lat=review_lat, map_lng=review_long, config=config, google_key=config2['google_key'],
                            row_loop=range(3), col_loop=range(4), areas=areas_json2, start=start,
                            walk=walk, favourite=favourite, stops=stops, criteria=criteria, photo_id=photo_id,
                            pubs=pubs_json, pub=pub_json, config2=config2, form_type='home', counter=counter)


