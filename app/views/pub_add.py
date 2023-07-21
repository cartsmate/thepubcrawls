import uuid
import pandas as pd
from datetime import datetime
from flask import render_template, request
from app import app
from app.models.pub.pub2 import *
from app.models.pub.pub_identity import PubIdentity
from app.models.review.review2 import Review2
from app.models.area.area import Area
from app.models.photo.photo import Photo
from app.models.station.station import Station
from config import Configurations
from app.static.pythonscripts.csv import Csv
# from app.static.pythonscripts.s3 import S3
from app.static.pythonscripts.dataframes import Dataframes
from app.static.pythonscripts.entities_multi import EntitiesMulti
from app.static.pythonscripts.controls_list import ControlsList
from app.static.pythonscripts.uuid import Uuid

config = Configurations().get_config()
config2 = Configurations().get_config2()


# @app.route("/pub/add/<lat>/<lng>")
# def pub_add(lat, lng):
@app.route("/pub/add/")
def pub_add():
    print('pub_add')
    station = request.args.get('station')
    direction = request.args.get('direction')
    lat = request.args.get('lat')
    print(lat)
    lng = request.args.get('lng')
    print(lng)

    pub_id = uuid.uuid4()
    print('new id: ' + str(pub_id))
    pub_identity = PubIdentity(value=pub_id)

    inst_pub = Pub2()
    inst_review = Review2()
    inst_pub.__dict__.update(inst_review.__dict__)
    inst_station = Station()
    inst_pub.__dict__.update(inst_station.__dict__)
    inst_pub_review = inst_pub
    alias = {}
    for k, v in inst_pub_review.__dict__.items():
        alias[k] = v.alias

    df_stations = Csv().get_stations()
    stations_json = Dataframes().df_to_dict(df_stations)

    df_areas = Csv().get_areas()
    areas_json = Dataframes().df_to_dict(df_areas)

    df_pubs = Csv().get_records('pub')
    df_pubs_stations = pd.merge(df_pubs, df_stations, how='left', on='station_identity')

    df_reviews = Csv().get_records('review')
    df_pubs_stations_reviews = pd.merge(df_pubs_stations, df_reviews, how='left', on='pub_identity')
    df_pubs_stations_reviews['colour'] = '#d9534f'

    if station != 'all':
        df_selected = df_pubs_stations_reviews.loc[df_pubs_stations_reviews['station_identity'] == station]
    elif direction != 'all':
        df_selected = df_pubs_stations_reviews.loc[df_pubs_stations_reviews['direction_identity'] == direction]
    else:
        df_selected = df_pubs_stations_reviews


    if lat is not None:
        review_lat = lat
        review_long = lng
    else:
        list_L = df_selected[['pub_latitude', 'pub_longitude']].values.tolist()
        _lat = []
        _long = []
        for l in list_L:
            _lat.append(l[0])
            _long.append(l[1])
        review_lat = sum(_lat) / len(_lat)
        review_long = sum(_long) / len(_long)
    # if lat != None:
    #     review_lat = lat
    #     review_long = lng
    # else:
    #     review_lat = df_selected['pub_latitude'].values[0]
    #     review_long = df_selected['pub_longitude'].values[0]

    dropdown_list, star_list, input_list, date_list, slider_list, check_list, alias_list, \
    required_list, form_visible_list, table_visible_list, icon_list, fields_list, ignore_list,\
    selected_pub_colour, other_pub_colour = ControlsList().get_control_lists()

    pubs_reviews_json = Dataframes().df_to_dict(df_pubs_stations_reviews)

    pub_attr_list = []
    pub_val_list = []
    for k, v in Pub2().__dict__.items():
        if k == 'pub_identity':
            pub_attr_list.append(v.name)
            print('id in loop: ' + str(pub_id))
            pub_val_list.append(str(pub_id))
        else:
            pub_attr_list.append(v.name)
            pub_val_list.append(v.value)
    # print(pub_attr_list)
    # print(pub_val_list)
    df_new_pub = pd.DataFrame(columns=pub_attr_list, data=[pub_val_list])
    print('new pub from class: df_new_pub:')
    print(df_new_pub[['pub_identity', 'pub_name', 'pub_deletion']])

    review_attr_list = []
    review_val_list = []
    for k, v in Review2().__dict__.items():
        if k == 'pub_identity':
            review_attr_list.append(v.name)
            print('id in loop: ' + str(pub_id))
            review_val_list.append(str(pub_id))
        else:
            review_attr_list.append(v.name)
            review_val_list.append(v.value)
    # print(review_attr_list)
    # print(review_val_list)
    df_new_review = pd.DataFrame(columns=review_attr_list, data=[review_val_list])
    df_new_review.fillna(' ', inplace=True)
    print(df_new_review)
    df_pub_review = pd.merge(df_new_pub, df_new_review, how="left", on='pub_identity')
    df_pub_review.fillna(' ', inplace=True)
    pub_json = Dataframes().df_to_dict(df_pub_review)

    diary_attr_list = []
    diary_val_list = []
    for k, v in Review2().__dict__.items():
        if k == 'pub_identity':
            diary_attr_list.append(k)
            print('id in loop: ' + str(pub_id))
            diary_val_list.append(str(pub_id))
        else:
            diary_attr_list.append(k)
            diary_val_list.append(k)
    df_new_diary = pd.DataFrame(columns=diary_attr_list, data=[diary_val_list])
    df_new_diary.fillna('', inplace=True)
    diary_json = Dataframes().df_to_dict(df_new_diary)

    diary_headers = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']

    return render_template("pub_read.html", form_type='add', google_key=config2['google_key'],
                           config=config, config2=config2, diary_body=diary_json,
                           map_lat=review_lat, map_lng=review_long,
                           pubs_selection=pub_json,
                           pubs_reviews=pubs_reviews_json,
                           star_list=star_list, dropdown_list=dropdown_list, input_list=input_list,
                           check_list=check_list, slider_list=slider_list, date_list=date_list,
                           alias_list=alias_list, icon_list=icon_list, alias=alias,
                           form_visible_list=form_visible_list,
                           table_visible_list=table_visible_list, required_list=required_list,
                           fields_list=fields_list, diary_headers=diary_headers,
                           stations=stations_json, areas=areas_json,
                           review_obj=Review2(), ignore_list=ignore_list)
