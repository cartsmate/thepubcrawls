import random

import botocore.exceptions
import time
import uuid
import pandas as pd
import numpy as np
from flask import render_template
from app import app
from config import Configurations
from app.static.pythonscripts.dataframes import Dataframes
from app.static.pythonscripts.csv import Csv
# from app.static.pythonscripts.s3 import S3
from app.static.pythonscripts.controls_list import ControlsList
from app.static.pythonscripts.entities_multi import EntitiesMulti
# from app.models.pub.pub2 import Pub2
from app.models.review.review2 import Review2
from app.models.diary.week import Week

config = Configurations().get_config()
config2 = Configurations().get_config2()


@app.route("/home/")
def home():
    dropdown_list, star_list, input_list, date_list, slider_list, check_list, alias_list, \
    required_list, form_visible_list, table_visible_list, icon_list, fields_list, \
    ignore_list = ControlsList().get_control_lists()

    directory_path = config2['directory_path']
    if config2['env'] == 'prod':
        obj_df = pd.read_csv(directory_path + '/files/counter_prod.csv')
    else:
        obj_df = pd.read_csv(directory_path + '/files/counter_qual.csv')
    obj_df["pub_counter"] = obj_df["pub_counter"] + 1

    if config2['env'] == 'prod':
        obj_df.to_csv(directory_path + '/files/counter_prod.csv', sep=',', encoding='utf-8', index=False)
    else:
        obj_df.to_csv(directory_path + '/files/counter_qual.csv', sep=',', encoding='utf-8', index=False)
    counter = str(obj_df["pub_counter"].values[0]).zfill(6)

    # try:
    # df_pubs = S3().get_s3_pubs()
    df_pubs = Csv().get_pubs().sort_values(by=['pub_name'], ascending=True)
    list_pub = []
    # list_of_pubs = df_pubs['pub_name'].values.tolist()
    for index, row in df_pubs.iterrows():
        # print("id: " + row['pub_identity'] + "| name: " + row['pub_name'])
        dict_pub = {'label': row['pub_name'], 'del': row['pub_deletion'], 'value': row['pub_identity']}
        list_pub.append(dict_pub)
    # print(list_pub)

    # list_of_pubs = df_pubs[['pub_identity', 'pub_name']].values.tolist()
    # for pub in list_of_pubs:
    #     json_pubs =

    df_stations = Csv().get_stations()
    stations_json = Dataframes().df_to_dict(df_stations)

    df_directions = Csv().get_directions()

    df_pub_with_station = pd.merge(df_pubs, df_stations, on='station_identity', how='left').sort_values(by='station_name')
    df_station_list = df_pub_with_station['station_name']
    df_station_unique = df_station_list.unique()
    list_stations = df_station_unique.tolist()

    unique_station_identity_list = df_pub_with_station['station_identity'].unique()
    df_unique_stations_identity = pd.DataFrame({'station_identity': unique_station_identity_list})
    df_unique_stations = pd.merge(df_unique_stations_identity, df_stations, on='station_identity', how='left')
    df_stations_directions = pd.merge(df_unique_stations, df_directions, on='direction_identity', how='left')
    df_stations_directions_trunc = df_stations_directions[['station_identity', 'station_name', 'direction_identity', 'direction_name']]
    stations_directions_list = df_stations_directions_trunc.values.tolist()
    # print(stations_directions_list)
    unique_directions_list = df_stations_directions['direction_identity'].unique()
    df_unique_directions_identity = pd.DataFrame({'direction_identity': unique_directions_list})
    df_unique_directions = pd.merge(df_unique_directions_identity, df_directions, on='direction_identity', how='left')
    df_unique_directions_trunc = df_unique_directions[['direction_identity', 'direction_name']]
    directions_list = df_unique_directions_trunc.values.tolist()

    pub_id = uuid.uuid4()
    l1 = list(Review2(pub_id).__dict__.keys())

    ignore_list = ['review_deletion', 'review_identity', 'pub_identity', 'detail']

    l3 = [x for x in l1 if x not in ignore_list]

    list_L = df_pubs[['pub_latitude', 'pub_longitude']].values.tolist()
    _lat = []
    _long = []
    for l in list_L:
        _lat.append(l[0])
        _long.append(l[1])

    review_lat = sum(_lat) / len(_lat)
    review_long = sum(_long) / len(_long)

    print("{:06d}".format(int(counter)))
    df_areas = Csv().get_areas()
    areas_json = Dataframes().df_to_dict(df_areas)

    diary_headers = []
    diary_week = Week().__dict__.items()
    for k, v in diary_week:
        diary_headers.append(k)
    # print(diary_headers)
    return render_template('home.html',
                           # list_areas=list_areas,
                           list_stations=list_stations,
                           areas=areas_json,
                           stations=stations_json, stations_directions_list=stations_directions_list,
                           map_lat=review_lat, map_lng=review_long, map_zoom=16,
                           diary_headers=diary_headers,
                           directions_list=directions_list,
                           # pubs_reviews=pubs_json, photo_array=config, map_view="stations",
                            config=config, google_key=config2['google_key'],
                            # row_loop=range(3), col_loop=range(4),
                           # start=start,
                           #  walk=walk, favourite=favourite, stops=stops, criteria=criteria, photo_id=photo_id,
                           #  pubs=pubs_json, pub=pub_json,
                            config2=config2, form_type='home',
                           counter=counter, list_of_pubs=list_pub, station='all', direction='all',
                           # no_all=no_all, no_reviewed=no_reviewed,
                           # no_all_2=no_all_2, no_reviewed_2=no_reviewed_2,
                            ignore_list=ignore_list, review_obj=Review2(pub_id), features=l3, icon_list=icon_list)
