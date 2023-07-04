import json
import pandas as pd
from flask import render_template, redirect, url_for, g, session, request
from app import app
from config import Configurations
from app.static.pythonscripts.dataframes import Dataframes
from app.static.pythonscripts.controls_list import ControlsList
from app.static.pythonscripts.csv import Csv
# from app.static.pythonscripts.s3 import S3
from app.static.pythonscripts.entities_multi import EntitiesMulti
from app.models.pub.pub2 import Pub2
from app.models.review.review2 import Review2
from app.models.area.area import Area
from app.models.station.station import Station

config = Configurations().get_config()
config2 = Configurations().get_config2()


# @app.route("/pub/list/<list_type>/<id_type>")
# def pub_list(list_type, id_type):
@app.route("/pub/list/")
def pub_list():
    print('pub_list')
    dropdown_list, star_list, input_list, date_list, slider_list, check_list, alias_list, \
    required_list, form_visible_list, table_visible_list, icon_list, fields_list, \
    ignore_list = ControlsList().get_control_lists()

    df_selection = EntitiesMulti().get_pubs_reviews()

    station = request.args.get('station')
    direction = request.args.get('direction')
    if request.args.get('station') != 'all':
        df_selection = df_selection.loc[df_selection['station_identity'] == station]
        heading = df_selection.iloc[0]['station_name']
    elif request.args.get('direction') != 'all':
        heading = direction
        df_selection = df_selection.loc[df_selection['direction_identity'] == direction]
    else:
        heading = 'All'

    review_list = {}
    for review in list(Review2().__dict__.keys()):
        if review not in ignore_list:
            # form_obj[review] = request.args.get(review)
            if request.args.get(review) == 'true':
                review_list[review] = ['True']
            else:
                review_list[review] = ['True', 'False']

    for review in review_list:
        df_selection = df_selection.loc[(df_selection[review].astype(str).isin(review_list[review]))]

    headers = list(df_selection.columns)

    inst_pub = Pub2()
    inst_review = Review2()
    inst_pub.__dict__.update(inst_review.__dict__)
    inst_area = Area()
    inst_pub.__dict__.update(inst_area.__dict__)
    inst_station = Station()
    inst_pub.__dict__.update(inst_station.__dict__)
    inst_pub_review = inst_pub
    visible = {}
    alias = {}
    for k, v in inst_pub_review.__dict__.items():
        visible[k] = v.table_visible
        alias[k] = v.alias

    form_obj = {}
    total_rows = df_selection.shape[0]
    if total_rows == 0:
        for review in list(Review2().__dict__.keys()):
            if review not in ignore_list:
                form_obj[review] = 'none'
        review_lat = 51.0
        review_long = -0.15
        data_list = []
        data_list = []
        for df in df_selection.columns:
            data_list.append(None)
        test_df = pd.DataFrame([data_list], columns=df_selection.columns)
        print(test_df)
        pubs_reviews_json = Dataframes().df_to_dict(test_df)

    else:
        list_L = df_selection[['pub_latitude', 'pub_longitude']].values.tolist()
        _lat = []
        _long = []
        for l in list_L:
            _lat.append(l[0])
            _long.append(l[1])
        review_lat = sum(_lat) / len(_lat)
        review_long = sum(_long) / len(_long)
        
        pubs_reviews_json = Dataframes().df_to_dict(df_selection)

        for review in list(Review2().__dict__.keys()):
            if review not in ignore_list:
                df_unique = df_selection[review].unique()
                list_unique = df_unique.tolist()
                if True in list_unique:
                    if False in list_unique:
                        form_obj[review] = 'some'
                    else:
                        form_obj[review] = 'all'
                else:
                    form_obj[review] = 'none'

    df_stations = Csv().get_stations()
    stations_json = Dataframes().df_to_dict(df_stations)

    return render_template('pub_list.html', filter=heading, pubs_reviews=pubs_reviews_json,
                           review_obj=Review2(),
                           map_lat=review_lat, map_lng=review_long, config2=config2,
                           form_type='list', google_key=config2['google_key'],
                           stations=stations_json, 
                           visible=visible, alias=alias, headers=headers, icon_list=icon_list,
                           form_obj=form_obj,
                           station=station, direction=direction, total_rows=total_rows)
