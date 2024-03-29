import random

import botocore.exceptions
import time
import uuid
import pandas as pd
import numpy as np
from flask import render_template, request
from app import app
from config import Configurations
from app.static.pythonscripts.dataframes import Dataframes
from app.static.pythonscripts.csv import Csv
# from app.static.pythonscripts.s3 import S3
from app.static.pythonscripts.controls_list import ControlsList
from app.static.pythonscripts.entities_multi import EntitiesMulti
from app.models.pub.pub2 import Pub2
from app.models.review.review2 import Review2
from app.models.area.area import Area
from app.models.station.station import Station
from app.models.direction.direction import Direction
from app.models.diary.week import Week

config = Configurations().get_config()
config2 = Configurations().get_config2()


@app.route("/home/", methods=['GET', 'POST'])
def home():
    dropdown_list, star_list, input_list, date_list, slider_list, check_list, alias_list, \
    required_list, form_visible_list, table_visible_list, icon_list, fields_list, \
    ignore_list, selected_pub_colour, other_pub_colour = ControlsList().get_control_lists()

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
    # df_pubs = Csv().get_pubs().sort_values(by=['pub_name'], ascending=True)

    df_pubs = pd.read_csv(directory_path + '/files/pubs.csv', dtype={'pub_identity': str, 'area_identity': str,
                                                                     'station_identity': str, 'pub_deletion': str,
                                                                     'pub_name': str, 'address': str, 'category': str,
                                                                     'colour': str, 'place': str, 'pub_latitude': float,
                                                                     'pub_longitude': float, 'rank': float,
                                                                     'detail': str})

    df_reviews = pd.read_csv(directory_path + '/files/reviews.csv', dtype={'review_deletion': str, 'brunch': str,
                                                                           'dart': str, 'entertain': str,
                                                                           'favourite': str, 'garden': str,
                                                                           'history': str, 'late': str,
                                                                           'music': str, 'pool': str, 'quiz': str,
                                                                           'roast': str, 'sport': str})

    df_diary = pd.read_csv(directory_path + '/files/diary.csv', dtype={'pub_identity': str, 'monday': str,
                                                                       'tuesday': str, 'wednesday': str,
                                                                       'thursday': str, 'friday': str,
                                                                       'saturday': str, 'sunday': str})
    # print('df_pubs')
    # print(df_pubs)
    # list_pub = []
    # # list_of_pubs = df_pubs['pub_name'].values.tolist()
    # for index, row in df_pubs.iterrows():
    #     # print("id: " + row['pub_identity'] + "| name: " + row['pub_name'])
    #     dict_pub = {'label': row['pub_name'], 'del': row['pub_deletion'], 'value': row['pub_identity']}
    #     list_pub.append(dict_pub)
    # print(list_pub)

    # list_of_pubs = df_pubs[['pub_identity', 'pub_name']].values.tolist()
    # for pub in list_of_pubs:
    #     json_pubs =

    # df_stations = Csv().get_stations()
    df_stations = pd.read_csv(directory_path + '/files/stations.csv',
                              dtype={'station_identity': str, 'station_deletion': str, 'station_name': str,
                                     'station_latitude': float, 'station_longitude': float, 'zone': str,
                                     'postcode': str, 'direction_identity': str})
    # stations_json = Dataframes().df_to_dict(df_stations)

    # df_directions = Csv().get_directions()
    df_directions = pd.read_csv(directory_path + '/files/directions.csv',
                                dtype={'direction_identity': str, 'direction_name': str, 'direction_deletion': str})

    df_pub_with_station = pd.merge(df_pubs, df_stations, on='station_identity', how='left').sort_values(by='station_name')
    # df_station_list = df_pub_with_station['station_name']
    # df_station_unique = df_station_list.unique()
    # list_stations = df_station_unique.tolist()

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
    # l1 = list(Review2(pub_id).__dict__.keys())

    # ignore_list = ['review_deletion', 'review_identity', 'pub_identity', 'detail']

    # l3 = [x for x in l1 if x not in ignore_list]

    list_L = df_pubs[['pub_latitude', 'pub_longitude']].values.tolist()
    _lat = []
    _long = []
    for l in list_L:
        _lat.append(l[0])
        _long.append(l[1])

    # review_lat = sum(_lat) / len(_lat)
    # review_long = sum(_long) / len(_long)

    # print("{:06d}".format(int(counter)))
    # df_areas = Csv().get_areas()
    # df_areas = pd.read_csv(directory_path + '/files/areas.csv',
    #                        dtype={'area_identity': str, 'area_deletion': str, 'area_name': str,
    #                               'area_type': str, 'area_latitude': float, 'area_longitude': float,
    #                               'parent_identity': str, 'photo_identity': str})
    # areas_json = Dataframes().df_to_dict(df_areas)

    # diary_headers = []
    diary_headers = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    # diary_week = Week().__dict__.items()
    # for k, v in diary_week:
    #     diary_headers.append(k)
    # print(diary_headers)

    # directory_path = config2['directory_path']
    # df_1 = pd.read_csv(directory_path + '/files/pubs.csv')
    # df_2 = pd.read_csv(directory_path + '/files/reviews.csv')
    # pubs_selection = pd.merge(df_1, df_2, on='pub_identity', how='left')
    # pubs_selection['colour'] = '#d9534f'
    # pub_review_json = Dataframes().df_to_dict(pubs_selection)

    # df_pubs = pd.read_csv(directory_path + '/files/pubs.csv', dtype={'pub_deletion': str})
    # df = pd.read_csv('test.csv', dtype={'pub_deletion': str, 'b': str})
    # all_data_json = Dataframes().df_to_dict(df_pubs)
    # print(all_data_json)
    # print(df_pubs.shape[0])

    df_rev_no_dupes = df_reviews.drop_duplicates(subset='pub_identity', keep="last")
    # df_reviews.groupby('pub_identity', group_keys=False).apply(lambda x: x.loc[x.review_identity.idxmax()])
    # df_areas = pd.read_csv(directory_path + '/files/areas.csv')
    # df_stations = pd.read_csv(directory_path + '/files/stations.csv', dtype={'station_deletion': str})
    # df_diary = pd.read_csv(directory_path + '/files/diary.csv')
    # df_directions = pd.read_csv(directory_path + '/files/directions.csv', dtype={'direction_deletion': str})

    df_pb_rev = pd.merge(df_pubs, df_rev_no_dupes, on='pub_identity', how='left')

    # df_pb_rev_ara = pd.merge(df_pb_rev, df_areas, on='area_identity', how='left')
    df_pb_rev_st = pd.merge(df_pb_rev, df_stations, on='station_identity', how='left')

    df_pb_rev_st_dir = pd.merge(df_pb_rev_st, df_directions, on='direction_identity', how='left')

    df_pb_rev_st_dir_dry = pd.merge(df_pb_rev_st_dir, df_diary, on='pub_identity', how='left')

    df_pb_rev_st_dir_dry = df_pb_rev_st_dir_dry.fillna('')
    df_missing = df_pb_rev_st_dir_dry.loc[df_pb_rev_st_dir_dry['pub_identity'] == '92c49a14-f650-4acc-a74f-b6fb96760631']
    print(df_missing)

    headers = list(df_pb_rev_st_dir_dry.columns)
    headers.append('distance')
    # print(df_pb_rev_st_dir_dry.dtypes)
    all_data_json = Dataframes().df_to_dict(df_pb_rev_st_dir_dry)

    inst_pub = Pub2()
    inst_review = Review2()
    inst_pub.__dict__.update(inst_review.__dict__)
    inst_area = Area()
    inst_pub.__dict__.update(inst_area.__dict__)
    inst_station = Station()
    inst_pub.__dict__.update(inst_station.__dict__)
    inst_direction = Direction()
    inst_pub.__dict__.update(inst_direction.__dict__)
    inst_pub_review = inst_pub
    visible = {}
    alias = {}

    for k, v in inst_pub_review.__dict__.items():
        # visible[k] = True
        if (k == 'station_name') and (request.args.get('station') != 'all'):
            visible[k] = 'false'
        else:
            visible[k] = v.table_visible
        alias[k] = v.alias

    diary_week = Week().__dict__.items()
    for k, v in diary_week:
        # visible[k] = True
        # if k == day:
        #     visible[k] = True
        # else:
        visible[k] = 'false'
        alias[k] = k
    alias['distance'] = 'distance'
    # print(alias)
    # print('visible')
    # print(visible)
    if request.method == 'GET':
        print('home/: GET')

        return render_template('home.html', pub_id='0',
                               # list_areas=list_areas,
                               # list_stations=list_stations, pubs_selection=all_data_json,
                               # areas=areas_json,
                               all_data=all_data_json,
                               # pubs_reviews=pub_review_json,
                               # stations=stations_json,
                               stations_directions_list=stations_directions_list,
                               # map_lat=review_lat, map_lng=review_long, map_zoom=16,
                               diary_headers=diary_headers,
                               headers=headers, visible=visible,
                               directions_list=directions_list,
                               fields_list=fields_list, required_list=required_list,
                               star_list=star_list, dropdown_list=dropdown_list, input_list=input_list,
                               check_list=check_list, slider_list=slider_list, date_list=date_list,
                               # pubs_reviews=pubs_json, photo_array=config, map_view="stations",
                                config=config, google_key=config2['google_key'], form_visible_list=form_visible_list,
                                # row_loop=range(3), col_loop=range(4),
                               # start=start,
                               #  walk=walk, favourite=favourite, stops=stops, criteria=criteria, photo_id=photo_id,
                               #  pubs=pubs_json, pub=pub_json,
                                config2=config2, form_type='home', alias=alias, alias_list=alias_list,
                               counter=counter,
                               # list_of_pubs=list_pub,
                               # station='all', direction='all',
                               # no_all=no_all, no_reviewed=no_reviewed,
                               # no_all_2=no_all_2, no_reviewed_2=no_reviewed_2,
                               #  ignore_list=ignore_list,
                                review_obj=Review2(pub_id),
                               # features=l3,
                               icon_list=icon_list)
            # ,
            #                    review_obj2=Review2(pub_id).__dict__.items())

    if request.method == 'POST':
        pub_id = request.args.get('pub_id')
        print('home/: POST: ' + pub_id)
        return render_template('home.html', pub_id=pub_id,
                               # list_stations=list_stations, pubs_selection=all_data_json,
                               # areas=areas_json,
                               all_data=all_data_json,
                               # pubs_reviews=pub_review_json,
                               # stations=stations_json,
                               stations_directions_list=stations_directions_list,
                               # map_lat=review_lat, map_lng=review_long, map_zoom=16,
                               diary_headers=diary_headers, headers=headers, visible=visible,
                               directions_list=directions_list,
                               fields_list=fields_list, required_list=required_list,
                               star_list=star_list, dropdown_list=dropdown_list, input_list=input_list,
                               check_list=check_list, slider_list=slider_list, date_list=date_list,
                               # pubs_reviews=pubs_json, photo_array=config, map_view="stations",
                               config=config, google_key=config2['google_key'], form_visible_list=form_visible_list,
                               # row_loop=range(3), col_loop=range(4),
                               # start=start,
                               #  walk=walk, favourite=favourite, stops=stops, criteria=criteria, photo_id=photo_id,
                               #  pubs=pubs_json, pub=pub_json,
                               config2=config2, form_type='home', alias=alias, alias_list=alias_list,
                               counter=counter,
                               # list_of_pubs=list_pub,
                               # station='all', direction='all',
                               # no_all=no_all, no_reviewed=no_reviewed,
                               # no_all_2=no_all_2, no_reviewed_2=no_reviewed_2,
                               # ignore_list=ignore_list,
                               review_obj=Review2(pub_id),
                               # features=l3,
                               icon_list=icon_list)
                                # ,review_obj2=Review2(pub_id).__dict__.items())
