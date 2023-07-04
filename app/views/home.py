import random

import botocore.exceptions
import time
import pandas as pd
import numpy as np
from flask import render_template
from app import app
from config import Configurations
from app.static.pythonscripts.dataframes import Dataframes
from app.static.pythonscripts.csv import Csv
from app.static.pythonscripts.s3 import S3
from app.static.pythonscripts.controls_list import ControlsList
from app.static.pythonscripts.entities_multi import EntitiesMulti
from app.models.pub.pub2 import Pub2
from app.models.review.review2 import Review2

config = Configurations().get_config()
config2 = Configurations().get_config2()


@app.route("/home/")
def home():
    dropdown_list, star_list, input_list, date_list, slider_list, check_list, alias_list, \
    required_list, form_visible_list, table_visible_list, icon_list, fields_list, \
    ignore_list = ControlsList().get_control_lists()

    # print(icon_list)
    directory_path = config2['directory_path']
    if config2['env'] == 'prod':
        # obj_df = S3().s3_read('counter_prod', ['pub_counter'])
        obj_df = pd.read_csv(directory_path + '/files/counter_prod.csv')
    else:
        # directory_path = os.getcwd()
        # directory_path = '/Users/andycarter/Documents/develop/thepubcrawls/'
        # directory_path = config2['directory_path']
        obj_df = pd.read_csv(directory_path + '/files/counter_qual.csv')

    obj_df["pub_counter"] = obj_df["pub_counter"] + 1

    if config2['env'] == 'prod':
        # s3_resp = S3().s3_write(obj_df, 'counter_prod.csv')
        obj_df.to_csv(directory_path + '/files/counter_prod.csv', sep=',', encoding='utf-8', index=False)
    else:
        # directory_path = os.getcwd()
        # directory_path = '/Users/andycarter/Documents/develop/thepubcrawls/'
        # directory_path = config2['directory_path']
        obj_df.to_csv(directory_path + '/files/counter_qual.csv', sep=',', encoding='utf-8', index=False)
    counter = str(obj_df["pub_counter"].values[0]).zfill(6)

    # directory_path = os.getcwd()
    # directory_path = '/Users/andycarter/Documents/develop/thepubcrawls/'
    # directory_path = config2['directory_path']

    # try:
    # df_pubs = S3().get_s3_pubs()
    df_pubs = Csv().get_pubs()
    # df_pubs.to_csv(directory_path + '/files/pubs.csv', index=False, sep=',', encoding='utf-8')
    # print(df_pubs)

    # df_reviews = S3().get_s3_reviews()
    # df_reviews.to_csv(directory_path + '/files/reviews.csv', index=False, sep=',', encoding='utf-8')

    # df_areas = S3().get_s3_areas()
    # df_areas = Csv().get_areas()
    # areas_json = Dataframes().df_to_dict(df_areas)
    # df_areas.to_csv(directory_path + '/files/areas.csv', index=False, sep=',', encoding='utf-8')

    # df_crawls = S3().get_s3_crawls()
    # df_crawls.to_csv(directory_path + '/files/crawls.csv', index=False, sep=',', encoding='utf-8')

    # df_stations = S3().get_s3_stations()
    df_stations = Csv().get_stations()
    stations_json = Dataframes().df_to_dict(df_stations)

    df_directions = Csv().get_directions()
    # print('df_directions')
    # print(df_directions)
    # df_stations.to_csv(directory_path + '/files/stations.csv', index=False, sep=',', encoding='utf-8')

    # df_photos = S3().get_s3_photos()
    # df_photos.to_csv(directory_path + '/files/photos.csv', index=False, sep=',', encoding='utf-8')

    # except botocore.exceptions.EndpointConnectionError:
    #     df_pubs = Csv().get_pubs()
    #     df_reviews = Csv().get_reviews()
    #     df_areas = Csv().get_areas()
    #     df_crawls = Csv().get_crawls()
    #     df_photos = Csv().get_photos()

    # start_time = time.time()
    # df_pubs_trunc = df_pubs[['pub_identity', 'area_identity']]
    # # print(df_pubs_trunc)
    # df_pubs_trunc_group = df_pubs_trunc.groupby(['area_identity'], as_index=False).count()
    # # print(df_pubs_trunc_group)
    # df_areas_count = pd.merge(df_pubs_trunc_group, df_areas, how='left', on='area_identity')\
    #     .sort_values(by=['area_name'], ascending=True)[['area_name']]
    # # print(df_areas_count)
    # list_areas = df_areas_count.values.tolist()
    # print(list_areas)
    #
    # print("--- %s seconds ---" % (time.time() - start_time))

    # start_time = time.time()
    # df_pubs_unique = df_pubs['area_identity'].unique()
    # df_x = pd.DataFrame({'area_identity': df_pubs_unique})
    # list_areas = pd.merge(df_areas, df_x, how='inner', on=['area_identity'])[['area_name']].values.tolist()
    # print(list_areas)
    # print("--- %s seconds ---" % (time.time() - start_time))

    # df_areas = Csv().get_areas()
    # df_pub_with_area = pd.merge(df_pubs, df_areas, on='area_identity', how='left').sort_values(by='area_name')
    # df_area_list = df_pub_with_area['area_name']
    # df_area_unique = df_area_list.unique()
    # list_areas = df_area_unique.tolist()

    # areas_json = Dataframes().df_to_dict(df_areas_count)
    # df_pubs_unique = df_pubs['station_identity'].unique()
    # df_x = pd.DataFrame({'station_identity': df_pubs_unique})
    # list_stations = pd.merge(df_stations, df_x, how='inner', on=['station_identity'])[['station_name']].values.tolist()

    df_pub_with_station = pd.merge(df_pubs, df_stations, on='station_identity', how='left').sort_values(by='station_name')
    df_station_list = df_pub_with_station['station_name']
    df_station_unique = df_station_list.unique()
    list_stations = df_station_unique.tolist()

    # df_pub_station_with_direction = pd.merge(df_pub_with_station, df_directions, on='direction_identity', how='left')
    # df_directions_unique = df_pub_station_with_direction['direction_identity'].unique()
    # df_unique = pd.DataFrame({'direction_identity': df_directions_unique})


    # list_directions = df_directions_unique.tolist()

    unique_station_identity_list = df_pub_with_station['station_identity'].unique()
    df_unique_stations_identity = pd.DataFrame({'station_identity': unique_station_identity_list})
    df_unique_stations = pd.merge(df_unique_stations_identity, df_stations, on='station_identity', how='left')
    df_stations_directions = pd.merge(df_unique_stations, df_directions, on='direction_identity', how='left')
    df_stations_directions_trunc = df_stations_directions[['station_identity', 'station_name', 'direction_identity', 'direction_name']]
    stations_directions_list = df_stations_directions_trunc.values.tolist()

    unique_directions_list = df_stations_directions['direction_identity'].unique()
    df_unique_directions_identity = pd.DataFrame({'direction_identity': unique_directions_list})
    df_unique_directions = pd.merge(df_unique_directions_identity, df_directions, on='direction_identity', how='left')
    df_unique_directions_trunc = df_unique_directions[['direction_identity', 'direction_name']]
    directions_list = df_unique_directions_trunc.values.tolist()
    # df_directions_trunc = df_directions[['direction_identity', 'direction_name']]
    # directions_list = df_directions_trunc.values.tolist()

    # PUB CRAWLS
    # df_crawl_last = df_crawls.tail(1)
    # start = df_crawl_last['start'].values[0]
    # walk = df_crawl_last['walk'].apply(str).values[0]
    # favourite = df_crawl_last['favourite'].values[0]
    # stops = df_crawl_last['stops'].apply(str).values[0]
    # criteria = df_crawl_last['criteria'].values[0]
    # df_pub = df_pubs.loc[df_pubs['place'] == start]
    # df_pub['colour'] = '#d9534f'
    # pub_json = Dataframes().df_to_dict(df_pub)

    # RANDOM PUB
    # df_pubs['colour'] = '#0275d8'
    # pubs_json = Dataframes().df_to_dict(df_pubs)
    # pubs_total = df_pubs.shape[0]
    # random_identity = random.randint(0, pubs_total)
    # pub_random = df_pubs.iloc[[random_identity]]
    # df = pd.merge(pub_random, df_photos, how='left', on='pub_identity')
    # photo_id = df['photo_identity'].values[0]

    # g = geocoder.ip('me')
    # print(g.latlng)
    # pub2 = Pub2()
    # pub3 = pub2.__dict__
    # for k, v in Review2().__dict__.items():
    #     # print(k)
    #     print(v.name)
    #     print(v.alias)
    #     print(v.icon)

    # for p in pub2.__init__():
    #     p
    l1 = list(Review2().__dict__.keys())
    # for l in l1:
    #     print(l)
    ignore_list = ['review_deletion', 'review_identity', 'pub_identity', 'detail']

    l3 = [x for x in l1 if x not in ignore_list]

    # df_all = Csv().get_pubs()
    # df_all_less_del = df_all[df_all["pub_deletion"] == "False"]
    # no_all = df_all_less_del.shape[0]
    # print(no_all)

    # df_pubs_less_del = df_pubs[df_pubs["pub_deletion"] == "False"]
    # no_all = df_pubs_less_del.shape[0]
    # print(no_all)
    #
    # df_group = df_pubs_less_del.groupby(['rank'], as_index=False).count()
    # no_0 = df_group[df_group['rank'] == 0]['pub_identity'].item()
    # print(no_0)
    #
    # no_reviewed = no_all - no_0

    list_L = df_pubs[['pub_latitude', 'pub_longitude']].values.tolist()
    _lat = []
    _long = []
    for l in list_L:
        _lat.append(l[0])
        _long.append(l[1])

    review_lat = sum(_lat) / len(_lat)
    review_long = sum(_long) / len(_long)

    print("{:06d}".format(int(counter)))

    return render_template('home.html',
                           # list_areas=list_areas,
                           list_stations=list_stations,
                           # areas=areas_json,
                           stations=stations_json, stations_directions_list=stations_directions_list,
                           map_lat=review_lat, map_lng=review_long, directions_list=directions_list,
                           # pubs_reviews=pubs_json, photo_array=config, map_view="stations",
                            config=config, google_key=config2['google_key'],
                            # row_loop=range(3), col_loop=range(4),
                           # start=start,
                           #  walk=walk, favourite=favourite, stops=stops, criteria=criteria, photo_id=photo_id,
                           #  pubs=pubs_json, pub=pub_json,
                            config2=config2, form_type='home',
                           counter=counter,
                           # no_all=no_all, no_reviewed=no_reviewed,
                           # no_all_2=no_all_2, no_reviewed_2=no_reviewed_2,
                            ignore_list=ignore_list, review_obj=Review2(), features=l3, icon_list=icon_list)
